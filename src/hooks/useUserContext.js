import { useContext } from "react";
import { UserContext } from "../context/UserContext";

export default function useUserContext() {
    return useContext(UserContext); 
}