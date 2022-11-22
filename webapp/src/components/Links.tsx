import React from 'react';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Link from '@mui/material/Link';
import TagLinkModal from './TagLinkModal';
import { getLinksBatchRequest, labelLinkRequest } from '../functions/requests';

interface Column {
  id: 'url' | 'title' | 'country' | 'keyword1' | 'keyword2';
  label: string;
  minWidth?: number;
  align?: 'left';
  format?: (value: number) => string;
}

const columns: readonly Column[] = [
  { id: 'url', label: 'URL', minWidth: 200 },
  {
    id: 'title',
    label: 'Title',
    minWidth: 100,
  },
  { id: 'country', label: 'País', minWidth: 100 },
  {
    id: 'keyword1',
    label: 'keywoard1',
    minWidth: 110,
  },
  {
    id: 'keyword2',
    label: 'keyword2',
    minWidth: 110,
  },
];

interface Data {
  id: string;
  url: string;
  country: string;
  keyword1: string;
  keyword2: string;
  title: string;
  label: string;
  createdAt: string;
  updatedAt: string;
}

function createData(
  id: string,
  url: string,
  title: string,
  country: string,
  keyword1: string,
  keyword2: string,
  label: string,
  createdAt: string,
  updatedAt: string
): Data {
  return {
    id,
    url,
    country,
    keyword1,
    keyword2,
    title,
    label,
    createdAt,
    updatedAt,
  };
}

const dummyRows = [
  createData(
    '1',
    'https://www.google.com',
    'title1 valuee',
    'Argentina',
    'keyword1 valuee',
    'keyword2 valuee',
    'yes',
    'created',
    'updated'
  ),
  createData(
    '2',
    'https://www.google.com',
    'title2 valuee',
    'Argentina',
    'keyword1 valuee',
    'keyword2 valuee',
    'no',
    'created',
    'updated'
  ),
  createData(
    '3',
    'https://www.google.com',
    'title3 valuee',
    'Argentina',
    'keyword1 valuee',
    'keyword2 valuee',
    '',
    'created',
    'updated'
  ),
  createData(
    '4',
    'https://www.google.com',
    'title4 valuee',
    'Argentina',
    'keyword1 valuee',
    'keyword2 valuee',
    'no',
    'created',
    'updated'
  ),
  createData(
    '5',
    'https://www.google.com',
    'title5 valuee',
    'Argentina',
    'keyword1 valuee',
    'keyword2 valuee',
    'maybe',
    'created',
    'updated'
  ),
  createData(
    '6',
    'https://www.google.com',
    'title6 valuee',
    'Argentina',
    'keyword1 valuee',
    'keyword2 valuee',
    'academic',
    'created',
    'updated'
  ),
  createData(
    '7',
    'https://www.google.com',
    'title6 valuee',
    'Argentina',
    'keyword1 valuee',
    'keyword2 valuee',
    '',

    'created',
    'updated'
  ),
  createData(
    '8',
    'https://www.google.com',
    'title6 valuee',
    'Argentina',
    'keyword1 valuee',
    'keyword2 valuee',
    '',
    'created',
    'updated'
  ),
];

const labelStyle = (label: string) => {
  switch (label) {
    case 'yes':
      return '#60D660';
    case 'no':
      return '#D66460';
    case 'maybe':
      return '#F0E666';
    case 'academic':
      return '#ff781f';
    default:
      return;
  }
};

const Links = () => {
  const [rows, setRows] = React.useState<Data[]>([]);
  const [open, setOpen] = React.useState(false);
  const [selectedLink, setSelectedLink] = React.useState<Data | null>(null);

  React.useEffect(() => {
    setRows(poblateTable(dummyRows));
    // getLinksBatchRequest({ size: 10 }).then((response: Data[]) => {
    //   setRows(poblateTable(response));
    // });
  }, []);

  function poblateTable(rows: Data[]) {
    let yesRows = rows.filter((row) => row.label === 'yes');
    let noRows = rows.filter((row) => row.label === 'no');
    let maybeRows = rows.filter((row) => row.label === 'maybe');
    let academicRows = rows.filter((row) => row.label === 'academic');
    let emptyRows = rows.filter((row) => row.label === '');
    return [...emptyRows, ...yesRows, ...noRows, ...maybeRows, ...academicRows];
  }

  const linkClickHandle = (link: Data): any => {
    setSelectedLink(link);
    setOpen(true);
  };

  const handleTagLink = (answer: string) => {
    const newRows = rows.map((row) => {
      if (row.id === selectedLink?.id) {
        // labelLinkRequest(row.id, answer).then((response) => {
        //   console.log(response);
        // });
        return { ...row, label: answer };
      }
      return row;
    });

    setRows(poblateTable(newRows));
    setOpen(false);
  };

  return (
    <Paper sx={{ width: '100%', overflow: 'hidden' }}>
      <TableContainer>
        <Table stickyHeader>
          <TableHead>
            <TableRow>
              {columns.map((column) => (
                <TableCell
                  key={column.id}
                  align={column.align}
                  style={{ minWidth: column.minWidth }}
                  sx={{ background: 'black', color: '#FFD369' }}
                >
                  {column.label}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => {
              return (
                <TableRow hover role="checkbox" tabIndex={-1} key={row.id}>
                  {columns.map((column) => {
                    const value = row[column.id];
                    return (
                      <TableCell
                        key={column.id}
                        align={column.align}
                        sx={{ backgroundColor: labelStyle(row['label']) }}
                      >
                        {column.id === 'url' ? (
                          <Link
                            href={value}
                            target="_blank"
                            rel="noopener noreferrer"
                            onClick={linkClickHandle(row)}
                          >
                            {value}
                          </Link>
                        ) : (
                          value
                        )}
                      </TableCell>
                    );
                  })}
                </TableRow>
              );
            })}
          </TableBody>
        </Table>
      </TableContainer>
      <TagLinkModal open={open} handleTagLink={handleTagLink} />
    </Paper>
  );
};

export default Links;
