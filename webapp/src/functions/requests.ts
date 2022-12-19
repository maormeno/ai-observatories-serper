// Path: webapp/src/functions/responses.ts
import axios from 'axios';

interface IGetLinksBatchRequest {
  size: number;
}

interface ILabelLinkRequest {
  linkId: string;
  label: string;
}

export const getLinksBatchRequest = async (request: IGetLinksBatchRequest) => {
  const { size } = request;
  const response = await axios.get(`http://127.0.0.1:8000/api/links/${size}`, {
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return response.data['links'];
};
export const getTestLinksRequest = async (half: number) => {
  const response = await axios.get(
    `http://127.0.0.1:8000/api/links/test/${half}`,
    {
      headers: {
        'Content-Type': 'application/json',
      },
    }
  );
  return response.data['links'];
};

export const labelLinkRequest = async (request: ILabelLinkRequest) => {
  const { linkId, label } = request;
  if (label === 'interesting') {
    const response = await axios.put(
      `http://127.0.0.1:8000/api/link/${linkId}`,
      {
        label: 'no',
        interesting: 1,
      }
    );
    return response.status;
  } else {
    const response = await axios.put(
      `http://127.0.0.1:8000/api/link/${linkId}`,
      {
        label,
        interesting: 0,
      }
    );
    return response.status;
  }
};
