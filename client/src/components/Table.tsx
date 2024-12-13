interface TableProps {
  headers: {
    key: string;
    link?: string;
    title: string;
  }[];
  data: Record<string, any>[];
}

export const Table = async (props: TableProps) => {
  return (
    <table>
      <thead>
        <tr>
          {props.headers.map((header) => (
            <th key={header.key}>{header.title}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {props.data.map((data, i) => (
          <tr key={i}>
            {props.headers.map((header) => (
              <td key={header.key}>
                {header.link ? (
                  <a href={`${header.link}${data[header.key]}`}>
                    {data[header.key]}
                  </a>
                ) : typeof data[header.key] === "object" ? (
                  JSON.stringify(data[header.key])
                ) : typeof data[header.key] === "boolean" ? (
                  <input type="checkbox" checked={data[header.key]} readOnly />
                ) : (
                  data[header.key]
                )}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};
