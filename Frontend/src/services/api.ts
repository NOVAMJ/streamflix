import axios from 'axios';
import { VideoOut } from '../types';

const API = axios.create({
  baseURL: 'http://localhost:8008/api/v1',
});

export const searchVideos = async (query: string): Promise<VideoOut[]> => {
  const response = await API.get(`/videos/search?query=${query}`);
  return response.data;
};

export default API;
