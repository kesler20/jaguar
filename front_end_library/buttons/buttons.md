```jsx
import styled from "styled-components";
import { Link } from "react-router-dom";

export const Cards = styled(Link)`
  text-decoration: none;
  font0-size:1.5rem;
  font-weight400;
  font-family: 'Lobster Two', cursive;
`;
export const Grid = styled.div`
  padding: 4rem 0rem;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  svg {
    font-size: 2rem;
  }
`;

export const DragBtn = styled.div`
  height: 60px;
  width: 60px;
  border-radius: 50%;
  background-color: darkcyan;
  color: #fff;
  border: none;
  font-size: 1.4em;
  cursor: pointer;
  box-shadow: 5px 5px 40px #000;
  outline: none;
`;

export const DangerBtn = styled.button`
  background: linear-gradient(
    90deg,
    rgba(255, 255, 0, 1) 0%,
    rgba(255, 59, 0, 1) 34%
  );
  border: none;
  color: white;
  border-radius: 20px;
  width: 100px;
  height: 60px;
`;

export const PrimaryBtn = styled.button`
  background: linear-gradient(
    90deg,
    rgba(76, 175, 80, 1) 0%,
    rgba(49, 220, 255, 1) 100%
  );
  border: none;
  color: white;
  border-radius: 20px;
  width: 100px;
  height: 60px;
`;

export const AddRowBtn = styled.div`
  height: 40px;
  width: 40px;
  border-radius: 50%;
  color: #8d38cd;
  border: none;
  font-size: 1em;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 5px 5px 40px rgb(158, 158, 158);
  outline: none;
  margin: 10% 30% 5%;

  :hover {
    box-shadow: 5px 5px 40px rgb(124, 121, 121);
  }
`;
```