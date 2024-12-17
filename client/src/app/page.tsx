"use client";

import axios from "axios";
import { useState } from "react";
import Popup from "@/components/Popup";

interface TaskProps {}

const Home = (props: TaskProps) => {
  const [formData, setFormData] = useState({
    name: "",
    description: "",
    file: null as File | null,
  });

  const [popup, setPopup] = useState<{ message: string; type: string } | null>(
    null
  );

  // Função para lidar com o envio do formulário
  const fetchTask = async (e: React.FormEvent) => {
    e.preventDefault(); // Previne o comportamento padrão do formulário

    // Criando um FormData para enviar arquivos
    const data = new FormData();
    data.append("name", formData.name);
    data.append("description", formData.description);
    if (formData.file) data.append("file", formData.file);

    try {
      const response = await axios.post(
        "http://localhost:8000/api/v1/task",
        data,
        {
          headers: {
            "Content-Type": "multipart/form-data", // Para envio de arquivos
          },
        }
      );

      // Tratando os status de sucesso ou aviso
      if (response.status === 200) {
        setPopup({ message: response.data.header.message, type: "success" });
      } else if (response.status === 300) {
        setPopup({ message: response.data.header.message, type: "warning" });
      }
    } catch (error: any) {
      // Tratando erros 400 ou 500
      if (error.response) {
        if (error.response.status === 400) {
          setPopup({
            message: error.response.data.header.message || "Failed Request",
            type: "failed",
          });
        } else if (error.response.status === 500) {
          setPopup({
            message: error.response.data.header.message || "Critical Error",
            type: "critical",
          });
        }
      } else {
        setPopup({
          message: "Erro inesperado. Verifique sua conexão.",
          type: "critical",
        });
      }
    }
  };

  // Função para atualizar os dados do formulário
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, files } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]: files ? files[0] : value, // Para arquivos, pega apenas o primeiro
    }));
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      {popup && <Popup message={popup.message} type={popup.type as any} />}
      <form
        onSubmit={fetchTask}
        className="flex flex-col shadow p-4 gap-4 bg-zinc-50"
      >
        <input
          className="bg-transparent focus:outline-none"
          type="text"
          name="name"
          placeholder="Nome"
          value={formData.name}
          onChange={handleChange}
        />
        <input
          className="bg-transparent focus:outline-none"
          type="text"
          name="description"
          placeholder="Descrição"
          value={formData.description}
          onChange={handleChange}
        />
        <input
          className="bg-transparent focus:outline-none"
          type="file"
          name="file"
          onChange={handleChange}
        />
        <button type="submit" className="bg-blue-500 text-white p-2 rounded">
          Enviar
        </button>
      </form>
    </div>
  );
};

export default Home;
