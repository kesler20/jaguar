Handling local storage

load everything from localstorage

```javascript
const storageSize = 1000;

const loadItemsFromLocalStorage = () => {
  let storedItems = [];
  for (let i = 0; i < storageSize; i++) {
    storedItems.push(localStorage.key(i));
  }
  return storedItems.filter((item) => item !== null);
};
```

clear everything from localstorage

```javascript
const [storageData, setStorageData] = useState([]);

const handleStorage = () => {
  if (!storageData) {
    localStorage.clear();
    setStorageData(true);
  } else {
    alert("By clicking this button Again you might lose all your files");
    setStorageData(false);
  }
};
```

Copying things to clipboard

```javascript
const handleCopy = () => {
  let elem = document.createElement("textarea");
  document.body.appendChild(elem);
  elem.value = JSON.stringify(nodes);
  elem.select();
  document.execCommand("copy");
  document.body.removeChild(elem);
  alert("Diagram Successfully Copied To Clipboard ☑️");
};
```

conditional rendering

```javascript

  const renderSideBar = (toRender) => {
    if (toRender) {
      return (
        <SideBar style={{ margin: "10px", color: "#e17bef" }}>
          <div className="avatar" data-tooltip="Save Diagram">
            <i className="fas fa-save fa-2x" onClick={onSaveDiagram} />
          </div>
          <div className="avatar" data-tooltip="Empty Storage">
            <i className="fas fa-trash fa-2x" onClick={handleStorage}></i>
          </div>
          <div className="avatar" data-tooltip="Load Diagram">
            <i
              className="fas fa-download fa-2x"
              onClick={onDownloadDiagram}
            ></i>
          </div>
        </SideBar>
      );
    } else {
      return "";
    }
  };

  <div>
    <div>
    {data.map((item) => {
      return <p key={item.id}>{item}</p>
    })}
    <div />
    {renderSideBar(sideBarView)}
  </div>
```


