import { useState } from "react";

export default function NewExerciseForm() {
  const [formData, setFormData] = useState({
    exercise_name: "",
    muscles_worked: "",
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
    <div className="new-exercise-form-container">
      <div className="page-title">new exercise form</div>
      <form onSubmit={handleSubmit}>
        <div className="new-exercise-form">
          <label htmlFor="exercise-name">exercise name </label>
          <input
            id="exercise-name"
            name="exercise_name"
            value={formData.exercise_name}
            type="text"
            className="exercise-name"
            onChange={handleFieldUpdate}
          />

          <label htmlFor="muscles-worked">muscles worked</label>
          <input
            id="muscles-worked"
            name="muscles_worked"
            value={formData.muscles_worked}
            type="text"
            className="muscles-worked"
            onChange={handleFieldUpdate}
          />

          <button type="submit">Add this exercise!</button>
        </div>
      </form>
    </div>
  );
}
