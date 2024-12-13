"use client";

import { useParams } from "next/navigation";
import Frame from "@/components/Frame";
import { Form } from "@/components/Form";
import { Input } from "@/components/Input";

const Job = () => {
  const params = useParams();
  const { id } = params;

  return (
    <Frame>
      <div className="flex items-center justify-center h-full">
        <Form title={`Job - ${id}`}>
          <Input id="title" type="text" label="Título" disabled={false} />
          <Input
            id="description"
            type="textarea"
            label="Descrição"
            disabled={false}
          />
          <Input
            id="periodicity"
            type="text"
            label="Periodicidade"
            disabled={false}
          />
          <Input
            id="args"
            type="textarea"
            label="Parâmetros"
            disabled={false}
          />
          <Input
            id="kwargs"
            type="textarea"
            label="Parâmetros nomeados"
            disabled={false}
          />
        </Form>
      </div>
    </Frame>
  );
};

export default Job;
