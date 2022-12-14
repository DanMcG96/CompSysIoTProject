const firebaseConfig = {
    apiKey: "AIzaSyBZT6GXivLSAMJ9p8wCispFCwd7PGcbRLo",
    authDomain: "sensepi-896f4.firebaseapp.com",
    databaseURL: "https://sensepi-896f4-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "sensepi-896f4",
    storageBucket: "sensepi-896f4.appspot.com",
    messagingSenderId: "149327982975",
    appId: "1:149327982975:web:d74a111245e8b5b3626a4a"
  };

firebase.initializeApp(firebaseConfig);

// Get a reference to the file storage service
const storage = firebase.storage();
// Get a reference to the database service
const database = firebase.database();

// Create camera database reference
const camRef = database.ref("file");

// Sync on any updates to the DB. THIS CODE RUNS EVERY TIME AN UPDATE OCCURS ON THE DB.
camRef.limitToLast(1).on("value", function(snapshot) {
  snapshot.forEach(function(childSnapshot) {
    const image = childSnapshot.val()["image"];
    const time = childSnapshot.val()["timestamp"];
    const storageRef = storage.ref(image);

    storageRef
      .getDownloadURL()
      .then(function(url) {
        console.log(url);
        document.getElementById("photo").src = url;
        document.getElementById("time").innerText = time;
      })
      .catch(function(error) {
        console.log(error);
      });
  });
});


