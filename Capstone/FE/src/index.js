import React from "react";
import ReactDOM from "react-dom/client";
import "./styles/common/common.scss";
import App from "./App";
import { BrowserRouter } from "react-router-dom/cjs/react-router-dom.min";
import { WorkoutContextProvider } from "./context/AppDataContext";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <WorkoutContextProvider>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </WorkoutContextProvider>
  </React.StrictMode>
);
