import { Module } from '@nestjs/common';
import { GetUltimoRegistroPlantaResolver } from './use-cases/get-ultimo-registro-planta/get-ultimo-registro-planta.resolver';
import { CreateRecordResolver } from './use-cases/create-record/create-record.resolver';
import { DeleteRecordByIdResolver } from './use-cases/delete-record-by-id/delete-record-by-id.resolver';
import { FindAllByPlantIdResolver } from './use-cases/find-all-by-plant-id/find-all-by-plant-id.resolver';
import { UpdateRecordByIdResolver } from './use-cases/update-record-by-id/update-record-by-id.resolver';
import { UpdateRecordByIdService } from './use-cases/update-record-by-id/update-record-by-id.service';
import { CreateRecordService } from './use-cases/create-record/create-record.service';
import { GetUltimoRegistroPlantaService } from './use-cases/get-ultimo-registro-planta/get-ultimo-registro-planta.service';
import { DeleteRecordByIdService } from './use-cases/delete-record-by-id/delete-record-by-id.service';
import { FindAllByPlantIdService } from './use-cases/find-all-by-plant-id/find-all-by-plant-id.service';
import { ValidationsService } from 'src/utils/validations.service';
import { PrismaService } from 'src/database/prisma/prisma.service';
import { JwtModule } from '@nestjs/jwt';
import { GetAllRecordsPaginatedResolver } from './use-cases/get-all-records-paginated/get-all-records-paginated.resolver';
import { GetAllRecordsPaginatedService } from './use-cases/get-all-records-paginated/get-all-records-paginated.service';
import { GetRecordResolver } from './use-cases/get-record/get-record.resolver';
import { GetRecordService } from './use-cases/get-record/get-record.service';
import { GeneratePdfResolver } from './use-cases/generate-pdf/generate-pdf.resolver';
import { GeneratePdfService } from './use-cases/generate-pdf/generate-pdf.service';
import { SpecieMapper } from '../species/specie-mapper.service';
import { GetRecordsAvgResolver } from './use-cases/get-records-avg/get-records-avg.resolver';
import { GetRecordsAvgService } from './use-cases/get-records-avg/get-records-avg.service';

@Module({
  imports: [JwtModule],
  providers: [
    GetUltimoRegistroPlantaResolver,
    CreateRecordResolver,
    DeleteRecordByIdResolver,
    FindAllByPlantIdResolver,
    UpdateRecordByIdResolver,
    UpdateRecordByIdService,
    FindAllByPlantIdService,
    DeleteRecordByIdService,
    GetUltimoRegistroPlantaService,
    CreateRecordService,
    ValidationsService,
    PrismaService,
    GetAllRecordsPaginatedResolver,
    GetAllRecordsPaginatedService,
    GetRecordResolver,
    GetRecordService,
    GeneratePdfResolver,
    GeneratePdfService,
    SpecieMapper,
    GetRecordsAvgResolver,
    GetRecordsAvgService,
  ],
})
export class RecordsModule {}
