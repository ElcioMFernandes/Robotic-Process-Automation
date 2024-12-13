import axios, { AxiosResponse } from "axios";

interface Job {
  id: string;
  title: string;
  periodicity: string;
  status: boolean;
}

async function fetchJobs(): Promise<Job[]> {
  try {
    const response: AxiosResponse<Job[]> = await axios.get(
      "http://127.0.0.1:8000/jobs"
    );
    return response.data; // Retorna os dados no formato tipado
  } catch (error) {
    console.error("Erro ao buscar os jobs:", error);
    throw error; // Repropaga o erro
  }
}
