/*
  Warnings:

  - You are about to alter the column `ofertas` on the `registro_aula` table. The data in that column could be lost. The data in that column will be cast from `Decimal(10,2)` to `DoublePrecision`.

*/
-- AlterTable
ALTER TABLE "registro_aula" ALTER COLUMN "ofertas" SET DATA TYPE DOUBLE PRECISION;
