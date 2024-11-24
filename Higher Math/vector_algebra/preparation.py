from Vector import *

st.set_page_config('Registratura')

st.title(
	'High Math'
)

with st.expander('📐📏Vectors'):
	a: Vector = Vector(
		[
			random.randint(-2, 4),
			random.randint(-2, 4),
			random.randint(-2, 4)
		]
	)

	b: Vector = Vector(
		[
			a[-1],
			random.randint(-2, 4),
			random.randint(-2, 4),
		]
	)

	angle: int = random.randint(0, 180)
	value: float = math.cos(math.radians(angle))
										
	with st.expander('Add vectors', icon='➕'):
		st.write(
			'Сложение векторов - это операция, при которой два вектора объединяются, \
			чтобы получить результирующий вектор a + b. При этом сумма a + b \
			двух векторов - это третий вектор c = a + b, проведённый из начала одного \
			вектора к концу второго, причём конец первого вектора совпадает с началом второго.'
		)

		c: Vector = a + b

		cols = st.columns([1, 1])
		with cols[0]:
			st.latex(
				r"""
				\vec{a} = (a_1, a_2, \dots, a_n)
				\\
				\vec{b} = (b_1, b_2, \dots, b_n)
				\\
				\vec{c} = (a_1 + b_1, a_2 + b_2, \dots, a_n + b_n)
				"""
			)

			
			st.latex(
				fr"""
				\vec{'{a}'} = ({a[0]}, {a[1]})
				\\
				\vec{'{b}'} = ({b[0]}, {b[1]})
				\\
				\vec{'{c}'} = ({a[0] + b[0]}, {a[1] + b[1]})
				"""
			)
		
		with cols[1]:
			figure, ax = plt.subplots()

			ax.quiver(*a[:-1], angles='xy', scale_units='xy', scale=1)
			ax.quiver(*a[:-1], *b[:-1], angles='xy', scale_units='xy', scale=1)
			ax.quiver(*c[:-1], angles='xy', scale_units='xy', scale=1, color='r')

			ax.set_xlim([-3, 6])
			ax.set_ylim([-3, 6])
			
			plt.grid()

			st.pyplot(figure)
				
	with st.expander('Sub vectors', icon='➖'):
		st.write(
			'Вычитание векторов - операция, обратная сложению, \
			ставящая в соответствие двум векторам третий вектор — \
			разность векторов, другими словами, по сумме векторов и одному \
			слагаемому определяется второе слагаемое этой суммы. При этом разность a - b \
			двух векторов a и b - это третий вектор c = a - b.'
		)

		c: Vector = a - b

		cols = st.columns([1, 1])
		with cols[0]:
			st.latex(
				r"""
				\vec{a} = (a_1, a_2, \dots, a_n)
				\\
				\vec{b} = (b_1, b_2, \dots, b_n)
				\\
				\vec{c} = (a_1 - b_1, a_2 - b_2, \dots, a_n - b_n)
				"""
			)

			
			st.latex(
				fr"""
				\vec{'{a}'} = ({a[0]}, {a[1]})
				\\
				\vec{'{b}'} = ({b[0]}, {b[1]})
				\\
				\vec{'{c}'} = ({a[0] - b[0]}, {a[1] - b[1]})
				"""
			)
		
		with cols[1]:
			figure, ax = plt.subplots()

			ax.quiver(*a[:-1], angles='xy', scale_units='xy', scale=1)
			ax.quiver(*b[:-1], angles='xy', scale_units='xy', scale=1)
			ax.quiver(*b[:-1], *c[:-1], angles='xy', scale_units='xy', scale=1, color='r')

			ax.set_xlim([-3, 6])
			ax.set_ylim([-3, 6])
			
			plt.grid()

			st.pyplot(figure)
	
	with st.expander('&#8594; Defining vector'):
		st.write(
			'Вектор - направленный отрезок, то есть отрезок, \
			для которого указано, какая из его граничных точек начало, а какая — конец.'
		)

		c: Vector = a.vector(b)

		cols = st.columns([1, 1])
		with cols[0]:
			st.latex(
				fr"""
				A = (A_1, A_2, \dots, A_n) \\
				B = (B_1, B_2, \dots, B_n) \\
				\overrightarrow{'{AB}'} = (B_1 - A_1, B_2 - A_2, \dots, B_n - A_n)
				"""
			)

			st.latex(
				fr"""
				A = ({a[0]}, {a[1]}) \\
				B = ({b[0]}, {b[1]}) \\
				\overrightarrow{'{AB}'} = ({c[0]}, {c[1]})
				"""
			)
		
		with cols[1]:
			figure, ax = plt.subplots()

			ax.quiver(*a[:-1], *c[:-1], angles='xy', scale_units='xy', scale=1, color='r')

			ax.set_xlim([-3, 6])
			ax.set_ylim([-3, 6])
			
			plt.grid()

			st.pyplot(figure)

	with st.expander('📏 Module(length) vector'):
		st.write(
			'Модулем вектора а называется число, равное длине отрезка а. Обозначается, как |a|.'
		)

		st.latex(
			fr"""
			{r'|\vec{a}|'} = (a_1, a_2, \dots, a_n)
			\\
			{r'|\vec{a}|'} = {'\sqrt{a_1^2 + a_2^2 + \dots + a_n^2} = \sqrt{\sum_{i=1}^{n}a_i^2}'}
			\\[20pt]
			{r'|\vec{a}|'} = ({a[0]}, {a[1]}, {a[2]})
			\\[3pt]
			{r'|\vec{a}|'} = {fr'\sqrt{'{'}{f'{a[0]}^2 + {a[1]}^2 + {a[2]}^2'}{f'{'} = '}{a.module}'}'}
			"""
		)
	
	with st.expander('&#8738; Direction cosines vector'):
		st.write(
			'Направляющие косинусы вектора a – это косинусы углов, \
			которые вектор образует с положительными полуосями координат.'
		)

		__cos: list[float] = a.single_vector
		module_a: float = a.module
		st.latex(
			fr"""
			{r'|\vec{a}|'} = (a_x, a_y, a_z)
			\\[8pt]
			{r'\cos\alpha = \frac{a_x}{|\vec{a}|};{\space\space}\cos\beta = \frac{a_y}{|\vec{a}|};{\space\space}\cos\gamma = \frac{a_z}{|\vec{a}|};'}
			\\[20pt]
			{r'\vec{a}'} = ({a[0]}, {a[1]}, {a[2]}){'\space' * 5}{r'|\vec{a}|'} = {module_a:.4f}
			\\[10pt]
			{r'\cos\alpha = \frac{'}{a[0]}{'}'}{'{'}{module_a:.3f}{'}'} = {__cos[0]:.2f};
			{'\space' * 2}
			{r'\cos\beta = \frac{'}{a[1]}{'}'}{'{'}{module_a:.3f}{'}'} = {__cos[1]:.2f};
			{'\space' * 2}
			{r'\cos\gamma = \frac{'}{a[2]}{'}'}{'{'}{module_a:.3f}{'}'} = {__cos[2]:.2f};
			"""
		)
	
	with st.expander('&#10178; Orthogonality vectors'):
		st.write(
			'Ортогональность векторов означает их перпендикулярность друг к другу. \
			В линейной алгебре два вектора называются ортогональными, \
			если их скалярное произведение равно нулю.'
		)

		orthogol: int | bool = a.orthogol(b)
		st.latex(
			fr"""
			{r'\vec{a}'} = (a_1, a_2, \dots, a_n)
			\\
			{r'\vec{b}'} = (b_1, b_2, \dots, b_n)
			\\
			{r'\vec{a}'} \cdot {r'\vec{b}'} = a_1 \cdot b_1 + a_2 \cdot b_2 + \dots + a_n \cdot b_n
			\\[20pt]
			{r'\vec{a}'} = ({a[0]}, {a[1]}, {a[2]})
			\\
			{r'\vec{b}'} = ({b[0]}, {b[1]}, {b[2]})
			\\
			{r'\vec{a}'} \cdot {r'\vec{b}'} = {a[0]} \cdot {b[0]} + {a[1]} \cdot {b[1]} + {a[2]} \cdot {b[2]} = {orthogol}
			\\[10pt]
			Скалярное{'\space'}произведение{'\space'}равно{'\space'}{orthogol} {r'\rightarrow'}  вектора{'\space'}{r'\vec{a},\space\vec{b}'}{'\space'}{'ортогональны' if orthogol == 0 else 'не\spaceортогональны'}
			"""
		)

	with st.expander('Collinearity vectors'):
		st.write(
			'Вектора, параллельные одной прямой или лежащие на одной прямой называют коллинеарными векторами.'
		)
		
		c: Vector = Vector(
			[
				[random.randint(1, 4), random.randint(-2, -1)][random.randint(0, 1)],
				random.randint(-2, 4),
				random.randint(-2, 4)
			]
		)

		n: str = rf'-\frac{abs(b[0])}{abs(c[0])}' if (b[0] / c[0]) < 0 else rf'\frac{abs(b[0])}{abs(c[0])}'
		collinear: Vector | bool = c.collinear(b)
		st.latex(
			fr"""
			{r'\vec{a}'} = (a_1, a_2, \dots, a_n)
			\\
			{r'\vec{b}'} = (b_1, b_2, \dots, b_n)
			\\[15pt]
			{r'\vec{b}'} = n \cdot {r'\vec{a}'}{'\space'}{'\space'}или{'\space'}{'\space'}
			{r'\frac{a_1}{b_1} = \frac{a_2}{b_2} = \dots = \frac{a_n}{b_n}'}
			\\[20pt]
			{r'\vec{a}'} = ({c[0]}, {c[1]}, {c[2]})
			\\
			{r'\vec{b}'} = ({b[0]}, {b[1]}, {b[2]})
			\\[10pt]
			n = {r'\frac{b_x}{a_x}'} = {n}
			\\[10pt]
			{n} \cdot {r'\vec{a}'} = {r'\vec{b}'}
			{r'\space\rightarrow'}
			({n} \cdot {c[0]}, {n} \cdot {c[1]}, {n} \cdot {c[2]}) = ({b[0]}, {b[1]}, {b[2]})
			{r'\space\rightarrow\\[5pt]'}
			({collinear[0]:.3f}, {collinear[1]:.3f}, {collinear[2]:.3f}) {'=' if collinear == b else r'\neq'} ({b[0]}, {b[1]}, {b[2]})
			{rf'\space\rightarrow\space вектора {'\space'}{r'\vec{a},\space\vec{b}'}{'\space'} {'коллинеарны' if collinear == b else 'не\spaceколлинеарны'}'}
			"""
		)
	
	with st.expander('&#8736; Projection vector'):
		st.write(
			'Проекция вектора — это длина отрезка, образованного проекциями точек \
			начала и конца вектора на заданную прямую. При этом проекции приписывается \
			знак плюс, если направление проекции соответствует направлению оси, иначе — знак минус.\
			\n\nПроекция вектора на ось — это скалярная величина (число), равная длине геометрической проекции вектора, \
			если направление оси и геометрической проекции совпадают, или число, противоположное \
			длине геометрической проекции вектора, если направления геометрической проекции и оси — противоположные.'
		)

		col = st.columns([1, 1])
		with col[0]:
			st.latex(
				fr"""
				{r'\vec{a}'} = (a_1, a_2, \dots, a_n)
				\\
				{r'\vec{b}'} = (b_1, b_2, \dots, b_n)
				\\[3pt]
				{r'\operatorname{pr}_{\vec{a}}{\vec{b}} = \frac{(\vec{a} \cdot \vec{b})}{|\vec{a}|}'}
				\\[20pt]
				{r'\vec{a}'} = ({a[0]}, {a[1]}, {a[2]})
				\\
				{r'\vec{b}'} = ({b[0]}, {b[1]}, {b[2]})
				\\[10pt]
				{f'{r'\operatorname{pr}_{\vec{a}}{\vec{b}} = \frac{'}{f'({a[0]} \cdot {b[0]} + {a[1]} \cdot {b[1]} + {a[2]} \cdot {b[2]})'}{f'{'}{'}{a.module:.4f}{'}'}'}'}
				\rightarrow
				\\[10pt]
				\rightarrow
				{f'{r'\operatorname{pr}_{\vec{a}}{\vec{b}} = \frac{'}{f'{a.scalar_mul(b)}'}{f'{'}{'}{a.module:.4f}{'}'}'}'}
				= {a.projection(b):.4f}
				\\[20pt]
				{r'\operatorname{pr}_{\vec{a}}{\vec{b}} = \frac{(\vec{a} \cdot \vec{b})}{|\vec{a}|} = {|\vec{b}|} \cdot \cos\phi \Rightarrow'}
				\\[8pt]\Rightarrow
				\cos\phi = {r'\frac{(\vec{a} \cdot \vec{b})}{|\vec{a}| \cdot {|\vec{b}|}}'}{'\space' * 10}
				\\[20pt]
				\cos\phi = {f'{r'\frac{'}{f'({a[0]} \cdot {b[0]} + {a[1]} \cdot {b[1]} + {a[2]} \cdot {b[2]})'}{f'{'}{'}{a.module:.3f} \cdot {b.module:.3f}{'}'}'}'}
				\rightarrow\\[7pt]\rightarrow
				\cos\phi = {f'{r'\frac{'}{f'{a.scalar_mul(b)}'}{f'{'}{'}{a.module:.3f} \cdot {b.module:.3f}{'}'}'}'} = {a.cos(b):.4f} = 
				\\[8pt]
				= {math.degrees(a.cos(b)):.3f}^\circ
				"""
			)
		
		with col[1]:
			st.latex(
				r"""
				\overrightarrow{AB} = (AB_1, AB_2, \dots, AB_n)
				\\
				\phi = angle^\circ or\space radians\rightarrow\cos\phi = value
				\\[5pt]
				\operatorname{pr}_{\vec{a}}{\overrightarrow{AB}} = |\overrightarrow{AB}| \cdot \cos{\phi}
				"""
			)

			st.image(
				'trig_circle.png',
				'Тригонометрическая окружность',
				width=300
			)

			st.latex(
				fr"""
				{r'\overrightarrow{AB}'} = ({a[0]}, {a[1]}, {a[2]})
				\\[2pt]
				\phi = {angle}^\circ \rightarrow \cos({angle}^\circ) = {value:.4f}
				\\[15pt]
				{r'\operatorname{pr}_{\vec{a}}{\overrightarrow{AB}} = '}{a.module:.4f} \cdot {value:.4f}
				\rightarrow
				\\[5pt]
				= {a.projection(angle=angle):.4f}
				"""
			)

	with st.expander('Scalar product vector'):
		st.write(
			'(Опредение из физики) Cкалярное произведение - произведение векторов a и b есть работа по \
			перемещению материальной точки из начала в конец вектора a под действием вектора силы b.'
		)

		st.write(
			'(Геометрическая интерпретация) Скалярным произведением двух векторов a и b \
			будет скалярная величина, равная произведению модулей этих векторов умноженного на косинус угла между ними.'
		)

		st.write(
			'(Алгебраическая интерпретация) Скалярным произведением двух векторов a и b \
			будет скалярная величина, равная сумме попарного произведения координат векторов a и b.'
		)

		col = st.columns([1, 1])
		with col[0]:
			st.latex(
				fr"""
				Алгебраическая\spaceинтерпретация
				\\[10pt]
				{r'\vec{a}'} = (a_1, a_2, \dots, a_n)
				\\
				{r'\vec{b}'} = (b_1, b_2, \dots, b_n)
				\\[3pt]
				{r'(\vec{a} \cdot \vec{b})'} = (a_1 \cdot b_1 + \dots + a_n \cdot b_n)
				\\[20pt]
				{r'\vec{a}'} = ({a[0]}, {a[1]}, {a[2]})
				\\
				{r'\vec{b}'} = ({b[0]}, {b[1]}, {b[2]})
				\\[3pt]
				{r'(\vec{a} \cdot \vec{b})'} = ({a[0]} \cdot {b[0]} + {a[1]} \cdot {b[1]} + {a[2]} \cdot {b[2]}) =
				\\[3pt]
				= {a.scalar_mul(b)}
				"""
			)
		
		with col[1]:
			st.latex(
				r"""
				Геометрическая\spaceинтерпретация
				\\[10pt]
				\vec{a} = (a_1, a_2, \dots, a_n)
				\\
				\vec{b} = (b_1, b_2, \dots, b_n)
				\\
				\phi = angle^\circ or\space radians\rightarrow\cos\phi = value
				\\[3pt]
				(\vec{a} \cdot \vec{b}) = |\vec{a}| \cdot |\vec{b}| \cdot \cos\phi
				"""
			)

			st.image(
				'trig_circle.png',
				'Тригонометрическая окружность',
				width=300
			)

			st.latex(
				fr"""
				{r'\vec{a}'} = ({a[0]}, {a[1]}, {a[2]})
				\\
				{r'\vec{b}'} = ({b[0]}, {b[1]}, {b[2]})
				\\[3pt]
				\\[2pt]
				\phi = {angle}^\circ \rightarrow \cos({angle}^\circ) = {value:.4f}
				\\[15pt]
				{r'(\vec{a} \cdot \vec{b})'} = {a.module:.3f} \cdot {b.module:.3f} \cdot {value:.4f} =
				\\[3pt]
				= {a.scalar_mul(b, angle):.4f}
				"""
			)
	
	with st.expander('Vector product'):

		st.write(
			'Векторное произведение векторов — это операция над двумя векторами в \
			трёхмерном пространстве, в результате которой получается новый вектор.'
		)

		st.write(
			'Векторное произведение двух векторов в трёхмерном евклидовом пространстве — вектор, \
			перпендикулярный обоим исходным векторам, длина которого численно равна \
			площади параллелограмма, образованного исходными векторами.'
		)
		
		vector_product: Vector = a * b
		st.latex(
			fr"""
			{r'\vec{a}'} = (a_x,\space a_y,\space a_z)
			\\
			{r'\vec{b}'} = (b_x,\space b_y,\space b_z)
			\\[15pt]
			{r'[\vec{a},\space\vec{b}] = \vec{a} \times \vec{b}'} = 
			{
				r"""
					\begin{vmatrix}
						\bar{\mathbf{i}} & \bar{\mathbf{j}} & \bar{\mathbf{k}} \\
						a_x & a_y & a_z \\
						b_x & b_y & b_z \\
					\end{vmatrix}
				"""
			}
			= 
			{
				r"""
				\bar{\mathbf{i}}
				\begin{vmatrix}
					a_y & a_z \\
					b_y & b_z \\
				\end{vmatrix}
				"""
			}
			-
			{
				r"""
				\bar{\mathbf{j}}
				\begin{vmatrix}
					a_x & a_z \\
					b_x & b_z \\
				\end{vmatrix}
				"""
			}
			+
			{
				r"""
				\bar{\mathbf{k}}
				\begin{vmatrix}
					a_x & a_y \\
					b_x & b_y \\
				\end{vmatrix}
				"""
			}
			\Rightarrow
			\\[10pt]\Rightarrow
			(a_y \cdot b_z - a_z \cdot b_y,\space -(a_x \cdot b_z - a_z \cdot b_x),\space a_x \cdot b_y - a_y \cdot b_x)
			\\[15pt]
			{r'\vec{a}'} = ({a[0]},\space {a[1]},\space {a[2]})
			\\
			{r'\vec{b}'} = ({b[0]},\space {b[1]},\space {b[2]})
			\\[15pt]
			{r'[\vec{a},\space\vec{b}] = \vec{a} \times \vec{b}'} = 
			{
				rf"""
					{
						r"""
							\begin{vmatrix}
							\bar{\mathbf{i}} & \bar{\mathbf{j}} & \bar{\mathbf{k}} \\
						"""
					}
						{a[0]} & {a[1]} & {a[2]} \\
						{b[0]} & {b[1]} & {b[2]} \\
					{r'\end{vmatrix}'}
				"""
			}
			= 
			{
				r"""
					\bar{\mathbf{i}}
					\begin{vmatrix}
				"""
			}
				{a[1]} & {a[2]} \\
				{b[1]} & {b[2]} \\
			{r'\end{vmatrix}'}
			-
			{
				r"""
					\bar{\mathbf{j}}
					\begin{vmatrix}
				"""
			}
				{a[0]} & {a[2]} \\
				{b[0]} & {b[2]} \\
			{r'\end{vmatrix}'}
			+
			{
				r"""
					\bar{\mathbf{k}}
					\begin{vmatrix}
				"""
			}
				{a[0]} & {a[1]} \\
				{b[0]} & {b[1]} \\
			{r'\end{vmatrix}'}
			=
			\\[10pt]
			= ({a[1]} \cdot {b[2]} - {a[2]} \cdot {b[1]},\space -({a[0]} \cdot {b[2]} - {a[2]} \cdot {b[0]}),\space {a[0]} \cdot {b[1]} - {a[1]} \cdot {b[0]})
			\\[5pt]
			= ({a[1] * b[2]} - {a[2] * b[1]},\space -({a[0] * b[2]} - {a[2] * b[0]}),\space {a[0] * b[1]} - {a[1] * b[0]}) = 
			({vector_product[0]},\space {vector_product[1]},\space {vector_product[2]})
			"""
		)
	
	with st.expander('&#9649; Area parallelogram'):
		st.write(
			'Площадь параллелограмма образованного векторами a и b равна модулю векторного произведения этих векторов'
		)

		cols = st.columns([1, 1])
		with cols[0]:
			vector_product: Vector = a * b
			st.latex(
				fr"""
				{r'\vec{a}'} = (a_1, a_2, \dots, a_n)
				\\
				{r'\vec{b}'} = (b_1, b_2, \dots, b_n)
				\\[3pt]
				S = {r'|\vec{a} \times \vec{b}|'}
				\\[15pt]
				{r'\vec{a}'} = ({a[0]}, {a[1]}, {a[2]})
				\\
				{r'\vec{b}'} = ({b[0]}, {b[1]}, {b[2]})
				\\[5pt]
				S = {r'|\vec{a} \times \vec{b}|'} = |({vector_product[0]},\space {vector_product[1]},\space {vector_product[2]})| = 
				\\[5pt]
				\sqrt{'{'}{sum([coord * coord for coord in vector_product])}{'}'} = {vector_product.module:.4f}
				"""
			)
		
		with cols[1]:
			figure, ax = plt.subplots()

			ax.quiver(*a[:-1], angles='xy', scale_units='xy', scale=1)
			ax.quiver(*b[:-1], angles='xy', scale_units='xy', scale=1)
			ax.quiver(*a[:-1], *b[:-1], angles='xy', scale_units='xy', scale=1, color='red')
			ax.quiver(*b[:-1], *a[:-1], angles='xy', scale_units='xy', scale=1, color='red')

			ax.set_xlim([-3, 6])
			ax.set_ylim([-3, 6])
			
			plt.grid()

			st.pyplot(figure)		
	
	with st.expander('&#9651; Area triangle'):
		st.write(
			'Площадь треугольника образованного векторами a и b равна половине модуля векторного произведения этих векторов'
		)

		cols = st.columns([1, 1])
		with cols[0]:
			vector_product: Vector = a * b
			st.latex(
				fr"""
				{r'\vec{a}'} = (a_1, a_2, \dots, a_n)
				\\
				{r'\vec{b}'} = (b_1, b_2, \dots, b_n)
				\\[7pt]
				S = {r'\frac{1}{2}|\vec{a} \times \vec{b}|'}
				\\[15pt]
				{r'\vec{a}'} = ({a[0]}, {a[1]}, {a[2]})
				\\
				{r'\vec{b}'} = ({b[0]}, {b[1]}, {b[2]})
				\\[10pt]
				S = {r'\frac{1}{2}|\vec{a} \times \vec{b}|'} = {r'\frac{1}{2}'}|({vector_product[0]},\space {vector_product[1]},\space {vector_product[2]})| = 
				\\[10pt]
				{r'\frac{1}{2}'}\sqrt{'{'}{sum([coord * coord for coord in vector_product])}{'}'} = {.5 * vector_product.module:.4f}
				"""
			)
		
		with cols[1]:
			figure, ax = plt.subplots()

			ax.quiver(*a[:-1], angles='xy', scale_units='xy', scale=1)
			ax.quiver(*b[:-1], angles='xy', scale_units='xy', scale=1)
			ax.quiver(*b[:-1], *(a - b)[:-1], angles='xy', scale_units='xy', scale=1, color='red', headwidth=1, headlength=6)

			ax.set_xlim([-3, 6])
			ax.set_ylim([-3, 6])
			
			plt.grid()

			st.pyplot(figure)
	
	with st.expander('Coplanarity (mixed product)'):
		st.write(
			'Векторы называются компланарными, если при откладывании их от одной и той же точки они будут лежать в одной плоскости.'
		)
		
		st.write(
			'Компланарные векторы — это векторы, которые лежат в одной плоскости или параллельны одной плоскости.'
		)

		mixed_prod: int = a.mixed_mul(b, c)

		st.latex(
			fr"""
			{r'\vec{a}'} = (a_1, a_2, \dots, a_n)
			\\
			{r'\vec{b}'} = (b_1, b_2, \dots, b_n)
			\\
			{r'\vec{c}'} = (c_1, c_2, \dots, c_n)
			\\[15pt]
			{r'\vec{a} \cdot [\vec{b} \times \vec{c}]'} = 
			{
				r"""
					\begin{vmatrix}
						a_x & a_y & a_z \\
						b_x & b_y & b_z \\
						c_x & c_y & c_z \\
					\end{vmatrix}
				"""
			}
			= 
			{
				r"""
				a_x
				\begin{vmatrix}
					b_y & b_z \\
					c_y & c_z \\
				\end{vmatrix}
				"""
			}
			-
			{
				r"""
				a_y
				\begin{vmatrix}
					b_x & b_z \\
					c_x & c_z \\
				\end{vmatrix}
				"""
			}
			+
			{
				r"""
				a_z
				\begin{vmatrix}
					b_x & b_y \\
					c_x & c_y \\
				\end{vmatrix}
				"""
			}
			\Rightarrow
			\\[10pt]\Rightarrow
			a_x \cdot (b_y \cdot c_z - b_z \cdot c_y) - (a_y \cdot (b_x \cdot c_z - b_z \cdot c_x)) + a_z \cdot (b_x \cdot c_y - b_y \cdot c_x)
			\\[15pt]
			{r'\vec{a}'} = ({a[0]},\space {a[1]},\space {a[2]})
			\\
			{r'\vec{b}'} = ({b[0]},\space {b[1]},\space {b[2]})
			\\
			{r'\vec{c}'} = ({c[0]},\space {c[1]},\space {c[2]})
			\\[15pt]
			{r'\vec{a} \cdot [\vec{b} \times \vec{c}]'} = 	
			{
				rf"""
					{
						r"""
							\begin{vmatrix}
						"""
					}
						{a[0]} & {a[1]} & {a[2]} \\
						{b[0]} & {b[1]} & {b[2]} \\
						{c[0]} & {c[1]} & {c[2]} \\
					{r'\end{vmatrix}'}
				"""
			}
			= 
			{a[0]}
			{
				r"""
					\begin{vmatrix}
				"""
			}
				{b[1]} & {b[2]} \\
				{c[1]} & {c[2]} \\
			{r'\end{vmatrix}'}
			-
			{a[1]}
			{
				r"""
					\begin{vmatrix}
				"""
			}
				{b[0]} & {b[2]} \\
				{c[0]} & {c[2]} \\
			{r'\end{vmatrix}'}
			+
			{a[2]}
			{
				r"""
					\begin{vmatrix}
				"""
			}
				{b[0]} & {b[1]} \\
				{c[0]} & {c[1]} \\
			{r'\end{vmatrix}'}
			=
			\\[10pt]
			= {a[0]} \cdot ({b[1]} \cdot {c[2]} - {b[2]} \cdot {c[1]}) - ({a[1]} \cdot ({b[0]} \cdot {c[2]} - {b[2]} \cdot {c[0]})) + {a[2]} \cdot ({b[0]} \cdot {c[1]} - {b[1]} \cdot {c[0]})
			\\[5pt]
			= {a[0]} \cdot ({b[1] * c[2]} - {b[2] * c[1]}) - ({a[1]} \cdot ({b[0] * c[2]} - {b[2] * c[0]})) +  {a[2]} \cdot ({b[0] * c[1]} - {b[1] * c[0]}) =
			\\[3pt]
			= {a[0]} \cdot ({b[1] * c[2] - b[2] * c[1]}) - ({a[1]} \cdot ({b[0] * c[2] - b[2] * c[0]})) +  {a[2]} \cdot ({b[0] * c[1] - b[1] * c[0]}) =
			\\[3pt]
			{a[0] * (b[1] * c[2] - b[2] * c[1])} - {a[1] * (b[0] * c[2] - b[2] * c[0])} +  {a[2] * (b[0] * c[1] - b[1] * c[0])} = {mixed_prod}
			\\[17pt]
			Векторное\spaceпроизведение - {mixed_prod} \rightarrow \space вектора{r'\space\vec{a}, \vec{b}, \vec{c}'}\space{'компланарны' if mixed_prod == 0 else 'не\spaceкомпланарны'}
 			"""
		)
	
	with st.expander('Volue pyramid'):
		st.write(
			'Объем пирамиды (объем тетраэдра) построенной на векторах a, b, c \
			равен шестой части модуля смешанного произведения векторов составляющих пирамиду'
		)

		st.latex(
			fr"""
			{r'\vec{a}'} = (a_x, a_y, a_z)
			\\
			{r'\vec{b}'} = (b_x, b_y, b_z)
			\\
			{r'\vec{c}'} = (c_x, c_y, c_z)
			\\[13pt]
			V = {r'\frac{1}{6}'}|{r'\vec{a} \cdot [\vec{b} \times \vec{c}]'}|
			\\[15pt]
			{r'\vec{a}'} = ({a[0]}, {a[1]}, {a[2]})
			\\
			{r'\vec{b}'} = ({b[0]}, {b[1]}, {b[2]})
			\\
			{r'\vec{c}'} = ({c[0]}, {c[1]}, {c[2]})
			\\[10pt]
			V = {r'\frac{1}{6}'}|{r'\vec{a} \cdot [\vec{b} \times \vec{c}]'}| = {r'\frac{1}{6}'} \cdot {a.mixed_mul(b, c)} = {a.pyramid(b, c):.3f}
			"""
		)

	with st.expander('Basis of vector'):
		st.write(
			'In process...'
		)
	
	with st.expander('Decomposition by basis'):
		st.write(
			'In process...'
		)

with st.expander('Matrix'):
	with st.expander('Add Matrix'):
		...
	
	with st.expander('Sub Matrix'):
		...
	
	with st.expander('Mul Matrix'):
		...
	
	with st.expander('Transponce Matrix'):
		...
	
	with st.expander('Detirminate Matrix'):
		...