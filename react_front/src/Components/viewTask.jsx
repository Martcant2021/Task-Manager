
import React, {useState, useEffect} from "react";
import { AddTask } from "./addTask";

export const ViewTask = () =>{

    const [task, setTask] = useState([])

    useEffect(()=>{
        fetch('/task').then(response =>{
            if(response.ok){
                return response.json()
            }
        }).then(data => setTask(data))
    }, [])

    return(
        <>
        <AddTask/>
        {task.map(task =>{
            return(
                <ul key = {task.id}>
                    <li>
                        {task.title},
                        {task.description},
                        {task.status}
                    </li>
                </ul>
            )
        })}
        </>
    )

}