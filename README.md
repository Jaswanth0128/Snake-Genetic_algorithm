# **Genetic Algorithms: Evolving Navigation Strategies for the Snake Game**

## **Project Overview**
This project implements Genetic Algorithms (GAs) integrated with a Feed-Forward Neural Network (FFNN) to evolve optimal navigation strategies for the classic Snake Game. The goal is to optimize the snake's ability to consume food while avoiding collisions with walls and itself. The dynamic and unpredictable nature of the game makes it an ideal environment for exploring artificial intelligence concepts such as optimization, decision-making, and pathfinding.

---

## **Demo Video**

https://github.com/user-attachments/assets/b72098f9-c258-4589-8a49-c431e913aa47

---

## **About the Case Study**

### **Title:** Genetic Algorithms: Evolving Navigation Strategies

### **Question:**
How can Genetic Algorithms combined with a Feed-Forward Neural Network be used to evolve optimal navigation strategies for the Snake Game?

### **Introduction:**
The Snake Game is a timeless arcade game where a snake must navigate a grid to consume food while avoiding collisions. Each time the snake consumes food, it grows longer, increasing the difficulty. This dynamic environment presents a challenging optimization problem. This case study explores how Genetic Algorithms can evolve efficient navigation strategies through selection, crossover, and mutation mechanisms.

### **Objectives:**
- To implement Genetic Algorithms for evolving optimal navigation strategies.
- To integrate a Feed-Forward Neural Network for decision-making.
- To analyze fitness score progression and evaluate the performance.

---

## **Project Structure**

- **`main.py`** — Starts the training process for evolving snake navigation strategies.
- **`Snake_Game.py`** — Contains the core logic for the Snake Game using Pygame.
- **`Run_Game.py`** — Runs the game using the best-evolved strategy.
- **`Genetic_Algorithm.py`** — Contains genetic algorithm functions including crossover and mutation.
- **`Feed_Forward_Neural_Network.py`** — Implements the feed-forward neural network for decision-making.

---

## **Pre-requisites**

### **1. Programming Environment**
- Python 3.7 or higher
- Pygame for game simulation
- NumPy for numerical operations
- Matplotlib for visualization

### **2. Installation**
```bash
pip install pygame numpy matplotlib
```

---

## **Execution**

### **1. Training the Snake Game**
Run the following command to start the training process with Genetic Algorithms:
```bash
python main.py
```

### **2. Running the Best Evolved Strategy**
To play the game using the best neural network model evolved through GAs:
```bash
python Run_Game.py
```

---

## **Tasks and Solutions**

### **Explanation of the Task:**
The snake must navigate the grid to consume food while avoiding collisions. Genetic Algorithms optimize the neural network weights to evolve better navigation strategies.

### **PEAS Description:**
- **Performance Measure:** Maximize food consumption and survival time.
- **Environment:** Grid-based dynamic environment.
- **Actuators:** Snake movement in four directions.
- **Sensors:** Snake's position, food location, and obstacles.

### **Task Environment Properties:**
- Fully observable
- Dynamic
- Sequential
- Stochastic
- Multi-agent (if extended to multiplayer)

### **Problem Formulation:**
- **State:** Current position of the snake and food.
- **Actions:** Move up, down, left, or right.
- **Transition Model:** Determines the next state after a move.
- **Reward:** Positive for food consumption, negative for collisions.

---

## **Explanation of the Algorithm Used**

### **Genetic Algorithm Process:**
1. **Initialization:** Randomly generate initial population of neural network weights.
2. **Selection:** Select top-performing chromosomes based on fitness scores.
3. **Crossover:** Combine parent chromosomes to produce offspring.
4. **Mutation:** Introduce small variations to offspring.
5. **Evaluation:** Measure fitness of new population.
6. **Iteration:** Repeat for multiple generations.

---

## **Visualization Output**

### **Fitness Score Progression Across Generations:**

![Figure_1](https://github.com/user-attachments/assets/62f7b2b2-2d08-42db-b548-2bbc8f02b230)


The plot illustrates the improvement in fitness scores across 100 generations, highlighting how the snake's performance improves over time.

---

## **Result Analysis**

The fitness score progression plot shows a consistent upward trend, indicating that the Genetic Algorithm effectively evolved better navigation strategies over time. Initial generations had high variance, while later generations stabilized with improved performance. Plateaus indicate possible local optima, suggesting that further parameter tuning could yield even better results.

If you want to check out every generation's fitness scores, check fitness_scores.txt
---

## **Output**

All fitness scores and generation logs are saved in `fitness_scores.txt`. The best-performing chromosome is stored for running the game.

---

## **Conclusion**

This project demonstrates the effectiveness of Genetic Algorithms in evolving complex behaviors in dynamic environments. By integrating a Feed-Forward Neural Network, the snake learns optimal strategies through iterative improvement. The result showcases how evolutionary algorithms can solve real-time optimization problems.

