import generate_instances
import algorithm
import draw_instances
import analyze_solutions
import analyze_instances
import draw_solution

generate_instances.main()
analyze_instances.main()
algorithm.main()
draw_instances.main()
analyze_solutions.main()

# ids retirados do arquivo results/examples.tex
draw_solution.main(0)
draw_solution.main(1)
draw_solution.main(5)
draw_solution.main(784)
