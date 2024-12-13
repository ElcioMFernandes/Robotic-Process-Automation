"use client";

import { useParams, useRouter } from "next/navigation";

const JobDetails = () => {
  const router = useRouter();
  const params = useParams();
  const id = params.id;

  const handleBack = () => {
    router.back();
  };
  return (
    <div>
      <div className="flex flex-row gap-4">
        <button onClick={handleBack}>Back</button>
        <h1>Detalhes do Job</h1>
      </div>
      <p>O ID do job é: {id}</p>
    </div>
  );
};

export default JobDetails;
