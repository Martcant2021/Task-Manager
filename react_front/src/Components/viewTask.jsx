
import React, {useState, useEffect} from "react";
import { AddTask } from "./addTask";

export const ViewTask = () =>{

    const [task, setTask] = useState([])
    const [addTask, setAddTask] = useState('')

    useEffect(()=>{
        fetch('/task').then(response =>{
            if(response.ok){
                return response.json()
            }
        }).then(data => setTask(data))
    }, [])

    const handleFormTask = (inputValue) =>{
        setAddTask(inputValue)

    }

    const  handleFormSubmit = () =>{
        fetch(`/task/create`, {
            method: 'POST',
            body: JSON.stringify({
                title:addTask
            }),
            headers: {
                "Content-Type": "application/json; charset=UTF-8"
            }
        }).then(response => response.json())
        .then(message =>{console.log(message)
        setAddTask('')
        allTask()
        },
            )
    }

    const allTask = () => {
        fetch(`/task`).then(response => response.json()
        ).then(data => setTask(data))
        .catch(error =>console.log(error));
    }

    const handleDeleteTask = (id) =>{
        fetch(`/task/delete/${id}`,{
            method: 'POST',
            body:JSON.stringify({
                id:id
            }),
            headers: {
                "Content-Type": "application/json; charset=UTF-8"
            }
        }).then(response => response.json())
        .then(data => {console.log(data)
        allTask()}
        )
        

    }



    return(
        <>
        <AddTask inputTask={addTask} onFormTask={handleFormTask} onFormSubmit={handleFormSubmit}/>
        {task.map(task =>{
            return(
                <ul key = {task.id} >
                    <li >
                        {task.title},
                        <button  onClick={()=> handleDeleteTask(task.id)}>Delete</button>
                    </li>
                </ul>
            )
        })}
        </>
    )

}