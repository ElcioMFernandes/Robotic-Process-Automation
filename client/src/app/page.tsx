import { Table } from "@/components/Table";
import { fetchJob } from "@/services/fetchJob";

const Home = async () => {
  const response = await fetchJob("http://127.0.0.1:8000/jobs");
  const headers = [
    { key: "id", title: "Identificador", link: "/job/" },
    { key: "title", title: "Título" },
    { key: "description", title: "Descrição" },
    { key: "periodicity", title: "Periodicidade" },
    { key: "args", title: "Argumentos" },
    { key: "kwargs", title: "Argumentos nomeados" },
    { key: "status", title: "Status" },
  ];

  return (
    <div>
      <Table headers={headers} data={response} />
    </div>
  );
};

export default Home;
