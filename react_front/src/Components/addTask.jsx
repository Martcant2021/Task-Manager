import React from "react";

export const AddTask = ({inputTask, onFormTask, onFormSubmit})=>{

    const  handleChange = (event) =>{
        onFormTask(event.target.value)
    }

    const  handleSubmit = (event) =>{
        event.preventDefault()
        onFormSubmit()
    }



    return(
        <>
        <form onSubmit={handleSubmit}>
            <input type="text" required value={inputTask} onChange={handleChange} />
            <input className="input" type="submit" />
        </form>
        </>

    )
}