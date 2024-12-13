interface ThProps {
  name: string;
  key: string;
  link?: string;
}

interface TrProps {
  [key: string]: React.ReactNode | boolean;
}

export interface TableProps {
  headers: ThProps[];
  data: TrProps[];
}
