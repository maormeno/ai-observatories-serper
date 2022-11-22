// Path: webapp/src/functions/responses.ts
import axios from 'axios';

interface IGetLinksBatchRequest {
  size: number;
}

export const getLinksBatchRequest = async (request: IGetLinksBatchRequest) => {
  const { size } = request;
  const response = await axios.get(`localhost:8000/api/links/${size}`);
  return response.data['links'];
};

export const labelLinkRequest = async (linkId: string, label: string) => {
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
