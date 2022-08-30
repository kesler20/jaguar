import { FormStyle } from "../components/StyledElements";
import { FaSearch } from "react-icons/fa";
import { useState, React } from "react";
import {useNavigate} from 'react-router-dom'
 
const Search = () => {
  const [input, setInput] = useState([]);
  const navigate = useNavigate()

  const submitHandler = (e) => {
    e.preventDefault();
    navigate('/searched/'+input)  
  };

  return (
    <FormStyle onSubmit={submitHandler}>
      <FaSearch></FaSearch>
        <input
          onChange={(e) => setInput(e.target.value)}
          type="text"
          value={input}
        />
    </FormStyle>
  );
};

export default Search;