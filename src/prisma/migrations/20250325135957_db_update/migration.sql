/*
  Warnings:

  - You are about to drop the `Post` table. If the table is not empty, all the data it contains will be lost.

*/
-- CreateEnum
CREATE TYPE "RoleUsuario" AS ENUM ('Professor', 'Admin', 'Superadmin', 'Aluno');

-- CreateEnum
CREATE TYPE "TipoIgreja" AS ENUM ('área', 'congregação');

-- CreateEnum
CREATE TYPE "EstadoFrequencia" AS ENUM ('Falta', 'Presença');

-- DropTable
DROP TABLE "Post";

-- CreateTable
CREATE TABLE "igreja" (
    "id" SERIAL NOT NULL,
    "nome" TEXT NOT NULL,
    "numero_da_area" TEXT,
    "endereco" TEXT,
    "pastor" TEXT,
    "superintendente" TEXT,
    "tipo" "TipoIgreja",

    CONSTRAINT "igreja_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "classe" (
    "id" SERIAL NOT NULL,
    "nome" TEXT NOT NULL,
    "nome_fantasia" TEXT,

    CONSTRAINT "classe_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "usuario" (
    "id" SERIAL NOT NULL,
    "igreja_id" INTEGER,
    "nome" TEXT NOT NULL,
    "telefone" TEXT,
    "email" TEXT NOT NULL,
    "senha" TEXT NOT NULL,
    "role_tipo" "RoleUsuario" NOT NULL,

    CONSTRAINT "usuario_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "turma" (
    "id" SERIAL NOT NULL,
    "nome" TEXT NOT NULL,
    "igreja_id" INTEGER,
    "classe_id" INTEGER,
    "professor_id" INTEGER,

    CONSTRAINT "turma_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "aluno" (
    "id" SERIAL NOT NULL,
    "nome" TEXT NOT NULL,
    "telefone" TEXT,
    "area_id" INTEGER,
    "turma_id" INTEGER,
    "classe_id" INTEGER,

    CONSTRAINT "aluno_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "registro_aula" (
    "id" SERIAL NOT NULL,
    "data" TIMESTAMP(3) NOT NULL,
    "trimestre" TEXT,
    "turma_id" INTEGER,
    "ofertas" DECIMAL(10,2),
    "biblias" INTEGER,
    "visitantes" INTEGER,
    "revistas" INTEGER,
    "total_de_assistencias" INTEGER,

    CONSTRAINT "registro_aula_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "frequencia_aluno" (
    "id" SERIAL NOT NULL,
    "aula_id" INTEGER NOT NULL,
    "aluno_id" INTEGER NOT NULL,
    "estado" "EstadoFrequencia" NOT NULL,

    CONSTRAINT "frequencia_aluno_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "usuario_email_key" ON "usuario"("email");

-- CreateIndex
CREATE UNIQUE INDEX "frequencia_aluno_aula_id_aluno_id_key" ON "frequencia_aluno"("aula_id", "aluno_id");

-- AddForeignKey
ALTER TABLE "usuario" ADD CONSTRAINT "usuario_igreja_id_fkey" FOREIGN KEY ("igreja_id") REFERENCES "igreja"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "turma" ADD CONSTRAINT "turma_igreja_id_fkey" FOREIGN KEY ("igreja_id") REFERENCES "igreja"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "turma" ADD CONSTRAINT "turma_classe_id_fkey" FOREIGN KEY ("classe_id") REFERENCES "classe"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "turma" ADD CONSTRAINT "turma_professor_id_fkey" FOREIGN KEY ("professor_id") REFERENCES "usuario"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "aluno" ADD CONSTRAINT "aluno_area_id_fkey" FOREIGN KEY ("area_id") REFERENCES "igreja"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "aluno" ADD CONSTRAINT "aluno_turma_id_fkey" FOREIGN KEY ("turma_id") REFERENCES "turma"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "aluno" ADD CONSTRAINT "aluno_classe_id_fkey" FOREIGN KEY ("classe_id") REFERENCES "classe"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "registro_aula" ADD CONSTRAINT "registro_aula_turma_id_fkey" FOREIGN KEY ("turma_id") REFERENCES "turma"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "frequencia_aluno" ADD CONSTRAINT "frequencia_aluno_aula_id_fkey" FOREIGN KEY ("aula_id") REFERENCES "registro_aula"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "frequencia_aluno" ADD CONSTRAINT "frequencia_aluno_aluno_id_fkey" FOREIGN KEY ("aluno_id") REFERENCES "aluno"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
