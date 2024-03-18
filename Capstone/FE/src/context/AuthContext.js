import { useContext, createContext, useState, useEffect } from "react";
import Cookies from "js-cookie";

const AuthContext = createContext();

export const useAuthInfo = () => {
  return useContext(AuthContext);
};
