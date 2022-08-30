const express = require("express");
const path = require("path");
const app = express();
const fs = require("fs");
const port = process.env.PORT || 5000;
app.use(express.static(path.join(__dirname, "public")));
app.use(express.json()); //  this is just to be able to send json data
app.use(express.urlencoded({ extended: false })); // this is just to be able to send form data

// include a;l your pages in the views folder
const viewsPath = path.join(__dirname, "views");

app.get("/", (req, res) => {
  res.sendFile(path.join(viewsPath, "index.html"));
});

// ----------------FOOD ----------------------------
app.get("/food", (req, res) => {
  res.sendFile(path.join(viewsPath, "food.html"));
});

app.post("/food", (req, res) => {
  console.log(createFood(req.body));
  res.sendFile(path.join(viewsPath, "food.html"));
});

app.get("/foodDatabase", (req, res) => {
  const db = new DatabaseApi("food.json");
  res.send(JSON.stringify(db.viewDatabase()));
});

// --------------- MEAL -----------------------------------

app.get("/meal", (req, res) => {
  res.sendFile(path.join(viewsPath, "meal.html"));
});

app.post("/meal", (req, res) => {
  createMeal(req.body);
  //console.log(createMeal(req.body));
  res.sendFile(path.join(viewsPath, "meal.html"));
});

app.get("/mealDatabase", (req, res) => {
  const db = new DatabaseApi("meal.json");
  res.send(JSON.stringify(db.viewDatabase()));
});

// --------------DIET -------------------------------

app.get("/diet", (req, res) => {
  res.sendFile(path.join(viewsPath, "diet.html"));
});

app.post("/diet", (req, res) => {
  createDietPlan(req.body);
  //console.log(createMeal(req.body));
  res.sendFile(path.join(viewsPath, "diet.html"));
});

  app.get("/dietDatabase", (req, res) => {
    // if you put relative imports the database will also put relative imports res) => {
  const db = new DatabaseApi("diet.json");
  res.send(JSON.stringify(db.viewDatabase()));
});

//TODO: remove the dependence on food
//TODO: store everything in lower case
// ---------------------- DATABASE ---------------
class DatabaseApi {
  constructor(fileName) {
    this.fileName = fileName;
  }

  createResource(resource) {
    //check for existing resources or if the resource is an object
    let existingResources = require(`./${this.fileName}`);
    let updatedResources = [...existingResources, resource];
    updatedResources = JSON.stringify(updatedResources);

    fs.writeFile(`./${this.fileName}`, updatedResources, "utf8", (err) => {
      if (err) {
        console.log("Failed to create resource 💩", err);
        return "";
      } else {
        console.log(`resource : ${updatedResources} created successfully✅`);
      }
    });
  }

  viewDatabase() {
    return require(`./${this.fileName}`);
  }

  getResource(resourceName) {
    let resource = require(`./${this.fileName}`);
    console.log(resource)
    return resource.filter((item) => item.name === resourceName);
  }
}

const createFood = (body) => {
  let food = {
    name: body.foodName,
    proteins: body.foodProtein,
    cost: body.foodCost,
    calories: body.foodCalories,
  };
  const db = new DatabaseApi("food.json");
  db.createResource(food);
  return food;
};

const createMeal = (body) => {
  let recipe = [];
  const db = new DatabaseApi("food.json");
  for (const ingredientIndex in body.foodName) {
    let ingredientName = body.foodName[ingredientIndex];
    let ingredientAmount = parseInt(body.foodAmount[ingredientIndex], 10) / 100;
    let ingredient = db.getResource(ingredientName)[0];
    ingredient.proteins = ingredientAmount * parseInt(ingredient.proteins, 10);
    ingredient.calories = ingredientAmount * parseInt(ingredient.calories, 10);
    ingredient.cost = ingredientAmount * parseInt(ingredient.cost, 10);
    recipe[ingredientIndex] = ingredient;
  }
  console.log(recipe);
  const meal = {
    name: body.mealName,
    recipe: recipe,
    total: calculateTotal(recipe),
  };

  // let initialMeal = JSON.stringify(meal)
  // initialMeal = `[${initialMeal}]`
  // fs.writeFile('meal.json',initialMeal , "utf8", (err) => {
  //   if (err) {
  //     console.log("Failed to create resource 💩", err);
  //     return "";
  //   } else {
  //     console.log(`resource : ${meal} created successfully✅`);
  //   }
  // });

  const dbMeal = new DatabaseApi("meal.json");
  dbMeal.createResource(meal);
  return meal;
};

const createDietPlan = (body) => {
  let meals = [];
  const db = new DatabaseApi("meal.json");
  console.log("body received", body);
  for (const mealIndex in body.mealName) {
    // when the meal on the diet is only one, this will return the first letter
    let mealName = body.mealName[mealIndex];
    let mealAmount = parseInt(body.mealAmount[mealIndex], 10) / 100;
    let meal = db.getResource(mealName)[0];
    meal.total[0] = mealAmount * parseInt(meal.total[0], 10);
    meal.total[1] = mealAmount * parseInt(meal.total[1], 10);
    meal.total[2] = mealAmount * parseInt(meal.total[2], 10);
    meals[mealIndex] = meal;
  }
  const dietPlan = {
    name: body.dietName,
    meals: meals,
    //total: calculateTotal(recipe),
  };

  // let initialDiet = JSON.stringify(dietPlan)
  // initialDiet = `[${initialDiet}]`
  // fs.writeFile('diet.json',initialDiet , "utf8", (err) => {
  //   if (err) {
  //     console.log("Failed to create resource 💩", err);
  //     return "";
  //   } else {
  //     console.log(`resource : ${initialDiet} created successfully✅`);
  //   }
  // });
  // if you put relative imports the database will also put relative imports
  const dbMeal = new DatabaseApi("diet.json");
  dbMeal.createResource(dietPlan);
  return dietPlan;
};



calculateTotal = (recipe) => {
  let totalProtein = 0;
  let totalCalories = 0;
  let totalCost = 0;

  recipe.forEach((ingredient) => {
    totalProtein = totalProtein + ingredient.proteins;
  });

  recipe.forEach((ingredient) => {
    totalCalories = totalCalories + ingredient.calories;
  });

  recipe.forEach((ingredient) => {
    totalCost = totalCost + ingredient.cost;
  });

  console.log("cost", totalCost);
  console.log("proteins", totalProtein);
  console.log("calories", totalCalories);
  return [totalCost, totalProtein, totalCalories];
};

app.listen(port, () => console.log(`🧐server started on ${port}`));