import { Args, Query, Resolver } from '@nestjs/graphql';
import { GraphQLError } from 'graphql';
import { PrismaService } from 'src/database/prisma/prisma.service';
import { ValidationsService } from 'src/utils/validations.service';
import { SpecieMapper } from '../../specie-mapper.service';
import { Specie } from '../../specie.type';
import { GetSpecieArgs } from './get-specie.args';

@Resolver()
export class GetSpecieResolver {
  constructor(
    private readonly prismaService: PrismaService,
    private readonly specieMapper: SpecieMapper,
    private readonly validationService: ValidationsService
  ) {}

  @Query(() => Specie)
  async getSpecie(@Args() args: GetSpecieArgs): Promise<Specie> {
    await this.prismaService.$connect();

    const { id } = args;

    if (!id) throw new GraphQLError('É necessário enviar um id para a consulta');

    if (id && !this.validationService.isObjectId(id)) throw new GraphQLError('ID inválido');

    const specie = await this.prismaService.especies.findUnique({
      where: { id, dataDeExclusao: null },
    });

    if (!specie) throw new GraphQLError('Espécie nao encontrada');

    await this.prismaService.$disconnect();

    return this.specieMapper.reverseMapParametros(specie);
  }
}
