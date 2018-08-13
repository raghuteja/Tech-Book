# Introduction to Artificial Intelligence

![](/assets/images/AI-Cycle.png)

The above cycle is known as perception action cycle

### Basic Terminology

#### Fully vs Partially Observable environment

| Fully Observable Environment | Partially Observable Environment |
| -- | -- |
| Fully observable environment is one in which the agent can always see the entire state of environment | Partially observable environment is one in which the agent can never see the entire state of environment |
| In case of fully observable environments all relevant portions of the environment are observable | In case of partially observable environments not all relevant portions of the environment are observable|
| Fully observable environment not need memory to make an optimal decision | Partially observable environment need memory to make an optimal decision |
| Ex: Checker Game, Chess | Ex: Card games where it requires previous state info |

#### Deterministic vs Stochastic environment

| Deterministic Environment | Stochastic Environment |
| -- | -- |
| In a deterministic environment, any action that is taken uniquely determines its outcome | In a stochastic environment, there is always some level of randomness|
| Ex: Chess, There is no uncertainty | Ex: Dice |

#### Discrete vs Continues environment

| Discrete Environment | Continues Environment |
| -- | -- |
| Discrete AI environments are those on which a finite set of possibilities can drive the final outcome of the task | Continuous AI environments rely on unknown and rapidly changing data sources |
| Chess is also classified as a discrete AI problem | Vision systems in drones or self-driving cars operate on continuous AI environments |

#### Benign vs Adversarial environment

| Benign Environment | Adversarial Environment |
| -- | -- |
| The environment has no objective that would "go against" what you're trying to accomplish | Environment will oppose what you're trying to do |
| Ex: weather | Ex: Competitive Games |


### AI and Uncertainty

AI as a technique of uncertainty management in computer software

**Reasons of uncertainty can be **
* Sensor limit
* Adversaries
* Stochastic
* Laziness
* Ignorance
