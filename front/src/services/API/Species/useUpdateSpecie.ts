import { useMutation, useQueryClient } from 'react-query';
import { useNotificacoes } from '../../../contexts/NotificacoesProvider';
import SMS_API, { GraphQLResponse } from '../sms-api';
import { MutationKeys, QueryKeys } from '../types';

interface Specie {
  id: string;
  nome: string;
  descricao: string;
  parametros: {
    nitrogenio: { min: string; max: string };
    fosforo: { min: string; max: string };
    potassio: { min: string; max: string };
    luz: { min: string; max: string };
    umidade: { min: string; max: string };
    temperatura: { min: string; max: string };
    pH: { min: string; max: string };
  };
}

interface SpecieQuery {
  updateSpecie: Specie;
}

const request = async (args: Specie) => {
  const { id, nome, descricao, parametros } = args;
  const token = `Bearer ${localStorage.getItem('token')}`;
  const options = { headers: { Authorization: token } };
  const variables = { id, nome, descricao, parametros };
  const query = `mutation UpdateSpecie($id: String!, $nome: String, $descricao: String, $parametros: UParametros) {
    updateSpecie(id: $id, nome: $nome, descricao: $descricao, parametros: $parametros) {
      id nome 
    }
  }`;

  return await SMS_API.post<GraphQLResponse<SpecieQuery>>('', { query, variables }, options);
};

export const useUpdateSpecie = (args: Specie) => {
  const queryClient = useQueryClient();
  const { notificar } = useNotificacoes();

  const onSucesso = () => {
    queryClient.invalidateQueries(QueryKeys.ALL_SPECIES);
    queryClient.invalidateQueries(QueryKeys.SPECIE);
    notificar({
      tipo: 'SUCESSO',
      mensagem: 'Espécie atualizada com sucesso',
    });
  };

  const {
    data,
    isLoading: updateSpecieIsLoading,
    mutate: confirmUpdateSpecie,
    error,
  } = useMutation({
    mutationFn: () => request(args),
    onSuccess: onSucesso,
    mutationKey: [MutationKeys.UPDATE_SPECIE],
    retry: false,
    onError: (e) => notificar({ mensagem: String(e), tipo: 'ERRO' }),
  });

  const specie = data?.data?.data?.updateSpecie;

  return {
    specie,
    updateSpecieError: error as string,
    updateSpecieIsLoading,
    confirmUpdateSpecie,
  };
};
