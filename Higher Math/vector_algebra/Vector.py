from utils import *

class Vector:

	def __init__(
			self, 
			coords: list[int | float] | set[int | float] | tuple[int | float]=None, 
			rows: int=None
		) -> None:

		if not (
			isinstance(coords, list) or \
			isinstance(coords, set) or \
			isinstance(coords, tuple) or \
			not coords
			):
			raise TypeError('Передан неверный формат координат.')
		
		if not (isinstance(rows, int) or not rows):
			raise TypeError('Передан неверный формат для вектора-столбца.')
		
		if coords:
			if len(coords) != rows and rows and rows != 1:
				raise Exception('Кол-во передаваемых координат не соответствует кол-ву строк для вектора-столбца.')
		
		self.__coords: list[int | float] | set[int | float] | tuple[int | float] = [i + 1 for i in range(3 if not rows else rows)] if not coords else coords
		self.__columns: int = 1 if rows and rows != 1 else len(self.__coords)
		self.__rows: int = rows if rows and rows != 1 else 1			
		
	@property
	def coords(self) -> list[int | float] | set[int | float] | tuple[int | float]:
		return self.__coords
	
	@property
	def rows(self) -> int:
		return self.__rows
	
	@property
	def columns(self) -> int:
		return self.__columns

	@property
	def module(self) -> float:
		return sum([coord ** 2 for coord in self]) ** .5

	@property
	def single_vector(self) -> typing.Self:
		"""
		Направляющий косинус
		"""
		return Vector(
			[
				coord / self.module
				for coord in self
			],
			self.__rows
		)
	
	def __print_vector(self) -> str:
		out: str = "("
		for rows in range(self.__rows):
			for columns in range(self.__columns):
				if self.__rows > 1:
					out += f'{'\n':47}'
				out += f'{self.__coords[rows * self.__columns + columns]}, '
		
		return out[::-1].replace(' ,', '', 1)[::-1] + f'{f'{'\n':43})' if self.__rows > 1 else ')'}'
	
	def __iter__(self) -> typing.Iterator:
		return self.__coords.__iter__()
	
	def __getitem__(self, index: int) -> int | float:
		return self.__coords[index]
	
	def vector(self, vector: typing.Self) -> typing.Self:
		if not isinstance(vector, Vector):
			raise TypeError("")
		
		return Vector(
			[
				vector[i] - self[i]
				for i in range(
					self.__rows 
					if self.__rows != 1 
					else self.__columns
				)
			],
			self.__rows
		)
	
	def scalar_mul(self, vector: typing.Self, angle: int | float=None) -> int | float:
		if angle:
			return self.module * vector.module * (math.cos(angle) if isinstance(angle, float) else math.cos(math.radians(angle)))
		
		return sum(
			[
				self[i] * vector[i] 
				for i in range(
					self.__rows 
					if self.__rows != 1 
					else self.__columns
				)
			]
		)
	
	def projection(self, vector: typing.Self=None, angle: int | float=None) -> float | int:
		if angle:
			return self.module * (math.cos(math.radians(angle)) if isinstance(angle, int) else math.cos(angle))
		
		return self.scalar_mul(vector) / vector.module

	def cos(self, vector: typing.Self) -> int | float:
		return self.scalar_mul(vector) / (self.module * vector.module)
	
	def triangle(self, vector: typing.Self) -> int | float:
		return .5 * (self * vector).module
	
	def parallelogram(self, vector: typing.Self) -> int | float:
		return (self * vector).module
	
	def collinear(self, vector: typing.Self) -> bool:
		n: float = vector[0] / self[0]
		#return vector == n * self
		return Vector(
					(n * self).coords
				)
	
	def orthogol(self, vector: typing.Self) -> bool:
		#return self.scalar_mul(vector) == 0
		return self.scalar_mul(vector)
	
	def mixed_mul(self, vector1: typing.Self, vector2: typing.Self) -> int | float:

		_sum: int | float = 0
		det: list[int | float] = self.coords + vector1.coords + vector2.coords
		for i in range(3):
			sing: int = (-1) ** i
			minor: list[int | float] = []
			minor_mul: int | float = det[i]
			for j in range(3):
				for k in range(3):
					if i != k:
						minor += [det[3 * j + k]]
			
			minor = minor[2:]
			_sum += (minor[0] * minor[-1] - minor[1] * minor[2]) * sing * minor_mul
		
		return _sum
	
	def pyramid(self, vector1: typing.Self, vector2: typing.Self) -> int | float:
		return abs(self.mixed_mul(vector1, vector2)) * (1 / 6)
						
	def __rules_sum(self, vector: typing.Self) -> bool:
		return self.__rows == vector.__rows and self.__columns == self.__columns

	def __add__(self, vector: typing.Self) -> typing.Self:
		if not isinstance(vector, Vector):
			raise TypeError("")
		
		if not self.__rules_sum(vector):
			raise Exception("")

		return Vector(
			[
				self[i] + vector[i] 
				for i in range(
					self.__rows 
					if self.__rows != 1 
					else self.__columns
				)
			],
			self.__rows
		)
	
	def __iadd__(self, vector: typing.Self) -> typing.Self:
		return self.__add__(vector)
	
	def __radd__(self, vector: typing.Self) -> typing.Self:
		return self.__add__(vector)
	
	def __sub__(self, vector: typing.Self) -> typing.Self:
		return self.__add__(
			Vector(
				[-coord for coord in vector],
				vector.__rows
			)
		)
	
	def __isub__(self, vector: typing.Self) -> typing.Self:
		return self.__sub__(vector)
	
	def __rsub__(self, vector: typing.Self) -> typing.Self:
		return self.__sub__(vector)
	
	def __mul__(self, vector: typing.Self | int | float) -> typing.Self:
		if isinstance(vector, int) or isinstance(vector, float):
			return Vector(
				[
					coord * vector
					for coord in self
				],
				self.__rows
			)
		
		coords: list[int | float] = []
		det = ['i', 'j', 'k'] + self.coords + vector.coords
		for i in range(3):
			minor: list[int | float] = []
			sing: int = (-1) ** i
			for j in range(3):
				for k in range(3):
					if i != k and isinstance(det[3 * j + k], int):
						minor += [det[3 * j + k]]
			
			coords += [(minor[0] * minor[-1] - minor[1] * minor[2]) * sing]
		
		return Vector(
			coords,
			self.__rows
		)

	def __imul__(self, vector: typing.Self | int | float) -> typing.Self:
		return self.__mul__(vector)

	def __rmul__(self, vector: typing.Self | int | float) -> typing.Self:
		return self.__mul__(vector)
	
	def __eq__(self, vector: typing.Self) -> bool:
		return all(
			[
				self.coords[i] == vector.coords[i] 
				for i in range(
					self.__rows 
					if self.__rows != 1 
					else self.__columns
				)
			]
		)
	
	def __contains__(self, item: int | float) -> bool:
		return any([item == coord for coord in self])

	def __str__(self) -> str:
		return f"""
			Вектор:
			  	Строки: {self.__rows}
			  	Столбцы: {self.__columns}
				Элементы: {self.__print_vector()}
		"""
	
if __name__ == '__main__':
	a = Vector([1, 2, 3])
	b = Vector(
		[4, 5, 6]
	)
	c = Vector([7, 8, -1])

	print(a, b, c, a.mixed_mul(b, c))