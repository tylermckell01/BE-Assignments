import { createContext, useContext, useState } from "react";

const WorkoutContext = createContext();

export const WorkoutContextProvider = ({ children }) => {
  const [yourWorkoutCards, setYourWorkoutCards] = useState([]);

  function handleSetYourWorkoutCards(value) {
    setYourWorkoutCards(value);
  }

  const values = { yourWorkoutCards, handleSetYourWorkoutCards };

  return (
    <WorkoutContext.Provider value={values}>{children}</WorkoutContext.Provider>
  );
};

export const useWorkoutContext = () => {
  return useContext(WorkoutContext);
};
