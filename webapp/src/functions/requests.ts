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
  const response = await axios.get(`http://127.0.0.1:8000/api/links/${size}/`);
  console.log(response);
  return response.data['links'];
};

export const labelLinkRequest = async (request: ILabelLinkRequest) => {
  const { linkId, label } = request;
  const response = await axios.put(`localhost:8000/api/link/${linkId}`, {
    label,
  });
  return response.status;
};

// const exportFunctions = {
//   getLinksBatchRequest,
//   labelLinkRequest,
// };

// export default exportFunctions;
