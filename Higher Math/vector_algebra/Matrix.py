from utils import *
from Vector import *

class Matrix:

	def __init__(
			self, 
			values: list[int | float] | None=None,
			rows: int | None=None, 
			columns: int | None=None
		) -> None:

		self.__rows = rows if rows else 3
		self.__columns = columns if columns else 3
		self.__values = values if values else [i for i in range(rows * columns if rows and columns else 9)]
	
	@property
	def get_rows(self) -> int:
		return self.__rows

	@property
	def get_columns(self) -> int:
		return self.__columns
	
	@property
	def get_values(self) -> list[int | float]:
		return self.__values
	
	def __add(self, matrix: typing.Self | Vector) -> bool:
		if not (isinstance(matrix, Matrix) or isinstance(matrix, Vector)):
			raise TypeError("")
		
		return self.__rows == matrix.__rows and self.__columns == matrix.__columns
		
	def __add__(self, matrix: typing.Self | Vector) -> typing.Self:
		if not self.__add(matrix):
			raise ValueError("")
		
		values: list[int | float] = []
		for i in range(self.__rows):
			for j in range(self.__columns):
				index: int = i * self.__rows + j
				values += [self.__values[index] + matrix.__values[index]]
		
		return Matrix(
			values,
			self.__rows,
			self.__columns
		)
	
	def __iadd__(self, matrix: typing.Self | Vector) -> typing.Self:
		return self.__add__(matrix)
	
	def __radd__(self, matrix: typing.Self | Vector) -> typing.Self:
		return self.__add__(matrix)
	
	def __sub__(self, matrix: typing.Self | Vector) -> typing.Self:
		for i in range(matrix.__rows):
			for j in range(matrix.__columns):
				matrix[i * matrix.__rows + j] *= -1

		return self.__add__(
			matrix
		)

	def __isub__(self, matrix: typing.Self | Vector) -> typing.Self:
		return self.__sub__(matrix)

	def __rsub__(self, matrix: typing.Self | Vector) -> typing.Self:
		return self.__sub__(matrix)
	
	def __mul(self, matrix: typing.Self | Vector) -> bool:
		if not (isinstance(matrix, Matrix) or isinstance(matrix, Vector)):
			raise TypeError("")
		
		return self.__columns == matrix.__rows
		
	def __mul__(self, matrix: typing.Self | Vector | int | float) -> typing.Self:
		if isinstance(matrix, int) or isinstance(matrix, float):
			for i in range(self.__rows):
				for j in range(self.__columns):
					self[i * self.__columns + j] *= matrix

			return self
		
		if not self.__mul(matrix):
			raise ValueError('')
		
		values: list[int | float] = []
		for i in range(self.__rows):
			for j in range(matrix.__columns):
				__sum: int | float = 0
				for k in range(self.__columns):
					__sum += self[i * self.__columns + k] * matrix[k * matrix.__columns + j]
				
				values += [__sum]
			
		return Matrix(
			values,
			self.__rows,
			matrix.__columns
		)

	def __imul__(self, matrix: typing.Self | Vector | int | float) -> typing.Self:
		return self.__mul__(matrix)
	
	def __rmul__(self, matrix: typing.Self | Vector | int | float) -> typing.Self:
		return self.__mul__(matrix)
	
	def __matmul__(self, matrix: typing.Self | Vector | int | float) -> typing.Self:
		return self.__mul__(matrix)

	def __imatmul__(self, matrix: typing.Self | Vector | int | float) -> typing.Self:
		return self.__matmul__(matrix)
	
	def __rmatmul__(self, matrix: typing.Self | Vector | int | float) -> typing.Self:
		return self.__matmul__(matrix)

	def __pow__(self, step: int) -> typing.Self:
		if step <= 0:
			raise ValueError('')
		
		tmp: int | Matrix = 1
		for _ in range(step):
			tmp *= self
		
		return tmp

	@property
	def T(self) -> typing.Self:
		values: list[int | float] = []
		for i in range(self.__columns):
			for j in range(self.__rows):
				values += [self[j * self.__columns + i]]
		
		return Matrix(
			values,
			self.__columns,
			self.__rows
		)

	def minor(self, rows: int, columns: int) -> typing.Self:
		if self.__rows != self.__columns:
			raise ValueError('')

		return Matrix(
			[
				self[i * self.__rows + j]
				for i in range(self.__rows)
				for j in range(self.__columns)
				if i != rows and j != columns
			],
			self.__rows - 1,
			self.__columns - 1
		)
	
	@property
	def det(self) -> int | float:
		if self.__rows != self.__columns:
			raise ValueError('')
		
		match self.__rows:
			case 1:
				return self[0]

			case 2:
				return self[0] * self[-1] - self[1] * self[2]
			
			case 3:
				return self[0] * self[4] * self[-1] + \
						self[1] * self[-3] * self[5] + \
						self[2] * self[3] * self[-2] - \
						self[2] * self[4] * self[-3] - \
						self[1] * self[3] * self[-1] - \
						self[0] * self[-2] * self[5]
			
			case self.__rows:
				__det: int | float = 0
				for i in range(self.__rows):
					sign: int = (-1) ** i
					__det += sign * self[i] * self.minor(0, i).det

					#minor: list[int | float] = []
					#for j in range(self.__rows):
					#	for k in range(self.__rows):
					#		if i != k and j != 0:
					#			minor += [self[j * self.__rows + k]]
			
					#__det += sign * self[i] * Matrix(minor, self.__rows - 1, self.__columns - 1).det

		return __det

	@property
	def E(self) -> typing.Self:
		if self.__rows != self.__columns:
			raise ValueError('')
		
		return Matrix(
			list(map(int, ' '.join(list(map(lambda x: ' '.join(list(map(str, x))), [[1 if i == j else 0 for j in range(self.__columns)] for i in range(self.__rows)]))).split())),
			self.__rows,
			self.__columns
		)
	
	def algebraic_addition(self, rows: int, columns: int) -> int | float:
		return (-1) ** (rows + columns) * self.minor(rows, columns).det
				
	@property
	def inverse(self) -> typing.Self | str:
		if self.__rows != self.__columns:
			raise ValueError('')
		
		if self.det == 0:
			return '0'
		
		return Matrix(
			[
				self.algebraic_addition(i, j)
				for i in range(self.__rows)
				for j in range(self.__columns)
			],
			self.__rows,
			self.__columns
		).T * (1 / self.det)

	def kramer(self, matrix: typing.Self | Vector) -> typing.Self | str:
		if self.__rows != self.__columns:
			raise ValueError('')
		
		if matrix.__rows != self.__columns:
			raise ValueError('')
		
		if self.det == 0:
			return '0'

		return Matrix(
			[
				Matrix(
					self.T[:i * self.__rows] + matrix.__values + self.T[(i + 1) * self.__rows:],
					self.__rows,
					self.__columns
				).T.det / self.det
				for i in range(self.__rows)
			],
			matrix.__rows,
			matrix.__columns
		)
	
		#return self.inverse * matrix
	
	@property
	def rank(self) -> int:
		new_self = copy.deepcopy(self)
		__rows: int = 0
		for i in range(new_self.__columns):
			flag: bool = False
			for j in range(__rows, new_self.__rows):
				if new_self[j * new_self.__columns + i] != 0:
					flag: bool = True

					swap_index_1: int = __rows * new_self.__columns
					swap_index_2: int = j * new_self.__columns

					new_self[swap_index_1:swap_index_1 + new_self.__columns], new_self[swap_index_2:swap_index_2 + new_self.__columns] = \
					new_self[swap_index_2:swap_index_2 + new_self.__columns], new_self[swap_index_1:swap_index_1 + new_self.__columns]
					break
			
			if flag:
				for j in range(__rows + 1, new_self.__rows):
					coff: float = new_self[j * new_self.__columns + i] / new_self[__rows * new_self.__columns + i]
					for k in range(i, new_self.__columns):
						new_self[j * new_self.__columns + k] -= new_self[__rows * new_self.__columns + k] * coff
				
				__rows += 1
		
		return sum(
			[
				any(
					[
						new_self[i * new_self.__columns + j] != 0
						for j in range(new_self.__columns)
					]
				)
				for i in range(new_self.__rows)
			]
		)
	
	def __format_values(self) -> str:
		output = '[\n'
		
		for i in range(self.__rows):
			output += f'{'':30}'
			for j in range(self.__columns):
				output += f'{
					f'{self[i * self.__columns + j]:^6}'
					if isinstance(self[i * self.__columns + j], int)
					else
					f'{self[i * self.__columns + j]:.4f}{'':3}'
				}'
			
			output += '\n'
		
		output += f'{'':26}]'
		return output
	 
	def __iter__(self) -> typing.Iterator:
		return self.__values.__iter__()
	
	def __getitem__(self, index: int | tuple) -> int | float:
		"""..."""
		if isinstance(index, tuple):
			row, column = index
			return self.__values[row * self.__columns + column]

		return self.__values[index]
	
	def __setitem__(self, index: int, value: int | float) -> None:
		self.__values[index] = value

	def __str__(self) -> str:
		return f"""
		Кол-во строк: {self.__rows}
		Кол-во столбцов: {self.__columns}
		Значения: {self.__format_values()}
		"""
	
if __name__ == '__main__':
	pass