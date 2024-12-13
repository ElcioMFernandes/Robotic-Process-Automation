import { TableProps } from "@/interface/tableProps";

export const Table = (props: TableProps) => {
  return (
    <table className="table-auto border-collapse border-t border-gray-300 w-full text-center">
      <thead>
        <tr className="">
          {props.headers.map((header) => (
            <th
              key={header.key}
              className="border-gray-300 px-4 py-2 text-blue-500"
            >
              {header.name}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {props.data.map((row, rowIndex) => (
          <tr key={rowIndex} className="hover:bg-gray-300">
            {props.headers.map((header) => {
              const cellValue = row[header.key];

              return (
                <td
                  key={`${rowIndex}-${header.key}`}
                  className="px-4 py-2 border-t"
                >
                  {typeof cellValue === "boolean" ? (
                    <input
                      type="checkbox"
                      checked={cellValue}
                      readOnly
                      className="accent-blue-500 hover:accent-blue-500"
                    />
                  ) : header.link ? (
                    <a href={`${header.link}${cellValue}`} className="">
                      {cellValue}
                    </a>
                  ) : (
                    cellValue || "-"
                  )}
                </td>
              );
            })}
          </tr>
        ))}
      </tbody>
    </table>
  );
};
