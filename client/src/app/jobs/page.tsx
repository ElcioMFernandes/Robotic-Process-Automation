import Frame from "@/components/Frame";
import { Table } from "@/components/Table";
import { link } from "fs";

const Jobs = () => {
  const headers = [
    { name: "Identificador", key: "id", link: "/jobs/" },
    { name: "Título", key: "title" },
    { name: "Periodicidade", key: "periodicity" },
    { name: "Status", key: "status" },
  ];

  const data = [{}];

  return (
    <Frame>
      <Table headers={headers} data={data}></Table>
    </Frame>
  );
};

export default Jobs;
