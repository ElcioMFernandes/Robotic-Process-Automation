export interface Job {
  id: string;
  title: string;
  description: string;
  periodicity: string;
  args: any[];
  kwargs: Record<string, any>;
  status: boolean;
}
