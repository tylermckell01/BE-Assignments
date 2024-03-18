import { useState } from "react";

export default function NewGymForm() {
  const [formData, setFormData] = useState({
    gym_name: "",
    workout_name: "",
  });

  const handleFieldUpdate = (e) => {
    const { name, value } = e.target;

    setFormData((previous) => ({ ...previous, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log("you submitted correctly, now wire it up to your BE!!");
  };

  return (
    <div className="new-gym-form-container">
      <div className="page-title">new gym form</div>
      <form onSubmit={handleSubmit}>
        <div className="new-gym-form">
          <label htmlFor="gym-name">gym name</label>
          <input
            id="gym-name"
            name="gym_name"
            value={formData.gym_name}
            type="text"
            className="gym-name"
            onChange={handleFieldUpdate}
          />
          {/* select workouts associated with this gym below
          <select
            name="workout-name"
            id="workout_name"
            value={formData.workout_name}
            className="workout-name"
          ></select> */}
          <button type="submit">Add this gym!</button>
        </div>
      </form>
    </div>
  );
}
