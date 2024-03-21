import { useEffect, useState } from "react";
import { useAppData } from "../context/AppDataContext";
import Cookies from "js-cookie";

export default function MyWorkoutCards() {
  const [yourWorkoutData, setYourWorkoutData] = useState([]);

  useEffect(() => {
    fetchWorkoutData();
  }, []);

  const fetchWorkoutData = async () => {
    let authToken = Cookies.get("auth_token");
    await fetch("http://127.0.0.1:8086/workouts", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        auth: authToken,
      },
    })
      .then((res) => res.json())
      .then((data) => {
        setYourWorkoutData(data.result);
      });

    console.log("piece of state", yourWorkoutData);
  };

  const renderWorkoutdata = () => {
    console.log("render function", yourWorkoutData);
    return yourWorkoutData?.map((workout, idx) => {
      return (
        <div className="workout-info" key={idx}>
          {workout.workout_name}
          {workout.description}
          {workout.exercises}
          {/* {workout.results.length} */}
        </div>
      );
    });
  };

  return (
    <div className="my-workout-cards-container">
      <div className="cards-wrapper">here are your workout cards</div>
      <div>
        this will be a card
        {renderWorkoutdata()}
      </div>
    </div>
  );
}
