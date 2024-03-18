import { useEffect, useState } from "react";
import { useWorkoutContext } from "../context/AppDataContext";

export default function MyWorkoutCards() {
  const [yourWorkoutData, setYourWorkoutData] = useState([]);

  const URL = "http://127.0.0.1:8086/workouts";

  useEffect(() => {
    fetchWorkoutData();
  }, []);

  // const fetchWorkoutData = async () => {
  //   const response = await fetch(URL);

  //   const jsonData = await response.json();
  //   setYourWorkoutData(jsonData);
  // };

  const fetchWorkoutData = async () => {
    try {
      const response = await fetch(URL);
      if (!response.ok) {
        throw new Error("Failed to fetch data");
      }
      const jsonData = await response.json();
      setYourWorkoutData(jsonData);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div className="my-workout-cards-container">
      <div className="cards-wrapper">here are your workout cards</div>
      <div>
        this will be a card
        {yourWorkoutData.map((item) => (
          <div key={item.id}>{item.workout_name}</div>
        ))}
      </div>
    </div>
  );
}
