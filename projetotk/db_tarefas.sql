CREATE DATABASE db_tarefas;
USE db_tarefas;

CREATE TABLE tbl_usuarios (
    usu_codigo INT AUTO_INCREMENT PRIMARY KEY,
    usu_nome VARCHAR(255),
    usu_email VARCHAR(255)
);

CREATE TABLE tbl_tarefas (
    tar_codigo INT AUTO_INCREMENT PRIMARY KEY,
    tar_descricao VARCHAR(255),
    tar_setor VARCHAR(100),
    tar_prioridade VARCHAR(20),
    tar_status VARCHAR(20),
    tar_data DATE,
    usu_codigo INT,
    FOREIGN KEY (usu_codigo) REFERENCES tbl_usuarios(usu_codigo) ON DELETE CASCADE
);