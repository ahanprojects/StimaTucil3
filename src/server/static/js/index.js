let map;

// Application state
const state = {
  coords: [],
  graph_lines: [],
  markers: [],
  path: [],
  path_lines: [],
  info: null,
};

// Constants
const startEl = document.getElementById("start");
const endEl = document.getElementById("end");
const fileForm = document.getElementById("form");
const tableBody = document.getElementById("table-body");

// Event Listeners
startEl.addEventListener("change", (e) => {
  if (endEl.value != "Titik tujuan") {
    getPath(e.target.value, endEl.value);
  }
});

endEl.addEventListener("change", (e) => {
  if (startEl.value != "Titik asal") {
    getPath(startEl.value, e.target.value);
  }
});

fileForm.addEventListener("change", (e) => {
  readFile(e.target.files[0]);
});

// Input file reading in JS
async function readFile(file) {
  removeMarkers();
  removePathLines();
  removeGraphLines();
  removeOptions();

  state.info.close();

  const content = await file.text();
  const lines = content.split("\n");

  const nNodes = Number(lines[0]);

  let node_arr = [];
  let words = [];

  for (i = 1; i < lines.length - nNodes - 1; i++) {
    words = lines[i].split(" ");
    node_arr = [
      ...node_arr,
      {
        name: words.slice(2, words.length).join(" ").replace("\r", ""),
        position: {
          lat: Number(words[0]),
          lng: Number(words[1]),
        },
        connected: [],
      },
    ];
  }

  for (i = nNodes + 1; i < lines.length - 1; i++) {
    lines[i].split(" ").forEach((weight, index) => {
      if (Number(weight) != 0) {
        node_arr[i - nNodes - 1].connected = [
          ...node_arr[i - nNodes - 1].connected,
          {
            name: node_arr[index].name,
            weight: calculateWeight(node_arr[i - nNodes - 1], node_arr[index]),
          },
        ];
      }
    });
  }

  state.coords = node_arr;

  const bounds = new google.maps.LatLngBounds();
  state.coords.forEach((node) => {
    addMarker(node.position, node.name);
    bounds.extend(node.position);
  });

  state.coords.forEach((node) => {
    node.connected.forEach((conn) => {
      drawGraphLine(node, getNodeByName(conn.name), "#FF0000");
    });
  });

  addOptions(state.coords);

  map.fitBounds(bounds);

  return node_arr;
}

function getNodeByName(name) {
  return state.coords.filter((node) => node.name == name)[0];
}

function degToRad(angle) {
  return (angle * Math.PI) / 180;
}

function calculateWeight(node1, node2) {
  let lng1 = degToRad(node1.position.lng);
  let lng2 = degToRad(node2.position.lng);
  let lat1 = degToRad(node1.position.lat);
  let lat2 = degToRad(node2.position.lat);

  let lngDiff = lng2 - lng1;
  let latDiff = lat2 - lat1;

  let dist =
    2 *
    6371 *
    1000 *
    Math.asin(
      Math.sqrt(
        Math.pow(Math.sin(latDiff / 2), 2) +
          Math.pow(Math.sin(lngDiff / 2), 2) * Math.cos(lat1) * Math.cos(lat2)
      )
    );

  return dist;
}

// HTTP Request ke program python
async function getPath(start, end) {
  removePathLines();
  state.info.close();

  const res = await fetch("http://localhost:5000/compute-path", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      graph: state.coords,
      start: start,
      end: end,
    }),
  });

  const data = await res.json();

  state.path = data.path;
  let tableBodyContent = "";
  for (i = 0; i < state.path.length - 1; i++) {
    tableBodyContent += `
    <tr>
      <td>${state.path[i].name} - ${state.path[i + 1].name}<td>
      <td>${
        Math.round(
          calculateWeight(
            getNodeByName(state.path[i].name),
            getNodeByName(state.path[i + 1].name)
          ) * 1000
        ) / 1000
      }<td>
    <tr/>`;
    drawPathLine(
      getNodeByName(state.path[i].name),
      getNodeByName(state.path[i + 1].name),
      "#0000FF"
    );
  }

  tableBody.innerHTML = tableBodyContent;

  state.info = new google.maps.InfoWindow({
    content: `Jarak tempuh sekitar ${Math.round(getDistance() * 1000) / 1000}m`,
    position: getNodeByName(state.path[state.path.length - 1].name).position,
  });

  state.info.open(map);
}

function addOptions(arr) {
  arr.forEach((el) => {
    startEl.innerHTML += `<option value="${el.name}">${el.name}</option>`;
    endEl.innerHTML += `<option value="${el.name}">${el.name}</option>`;
  });
  startEl.removeAttribute("disabled");
  endEl.removeAttribute("disabled");
}

function removeOptions() {
  startEl.innerHTML = "";
  endEl.innerHTML = "";
  endEl.setAttribute("disabled", true);
  endEl.setAttribute("disabled", true);
}

// Map drawing utils
function addMarker(coords, title) {
  let newMarker = new google.maps.Marker({
    position: coords,
    title: title,
    label: title,
  });
  state.markers = [...state.markers, newMarker];
  newMarker.setMap(map);
}

function drawPathLine(start, dest, color) {
  let newPath = new google.maps.Polyline({
    path: [start.position, dest.position],
    geodesic: true,
    strokeColor: color,
    strokeOpacity: 1.0,
    strokeWeight: 2,
  });
  state.path_lines = [...state.path_lines, newPath];
  newPath.setMap(map);
}

function drawGraphLine(start, dest, color) {
  let newPath = new google.maps.Polyline({
    path: [start.position, dest.position],
    geodesic: true,
    strokeColor: color,
    strokeOpacity: 0.2,
    strokeWeight: 2,
  });
  state.graph_lines = [...state.graph_lines, newPath];
  newPath.setMap(map);
}

function removeMarkers() {
  state.markers.forEach((marker) => marker.setMap(null));
  state.markers = [];
}

function removePathLines() {
  state.path_lines.forEach((path) => path.setMap(null));
  state.path_lines = [];
}

function removeGraphLines() {
  state.graph_lines.forEach((path) => path.setMap(null));
  state.graph_lines = [];
}

function getDistance() {
  return state.path[state.path.length - 1].weight;
}

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -6.893667, lng: 107.610564 },
    zoom: 17,
  });

  state.info = new google.maps.InfoWindow({
    content: "",
  });
}
