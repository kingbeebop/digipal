export interface LoginData {
    username: string;
    password: string;
  }
  
  export interface AuthResponse {
    access_token: string;
    refresh_token: string;
  }