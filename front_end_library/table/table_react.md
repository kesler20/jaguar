```jsx
export const Table = styled.table`
  border-collapse: collapse;
  width: 100%;

  th {
    padding-top: 12px;
    padding-bottom: 12px;
    text-align: left;
    background-color: #9050cc;
    color: white;
  }

  td,
  th {
    border: 1px solid #ddd;
    padding: 8px;
  }

  tr:nth-child(even) {
    background-color: #f2f2f2;
  }

  tr:hover {
    background-color: #ddd;
  }

  input {
    background: transparent;
    border: none;
    border-bottom: 1px solid black;
    outline: none;
    font-size: 17px;
  }
`;
```