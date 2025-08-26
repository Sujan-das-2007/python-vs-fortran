! operators_functions_print.f90
program basics
  implicit none   ! forces variable declaration (good practice)

  ! Declare variables
  integer :: a, b, result
  real    :: x, y, z
  logical :: flag

  ! Assign values
  a = 10
  b = 3
  x = 5.0
  y = 2.5

  ! --- Arithmetic Operators ---
  print *, "=== Arithmetic Operators ==="
  print *, "a + b =", a + b          ! addition
  print *, "a - b =", a - b          ! subtraction
  print *, "a * b =", a * b          ! multiplication
  print *, "a / b =", a / b          ! integer division (result = 3)
  print *, "a / real(b) =", a / real(b)  ! convert to real → 3.3333
  print *, "a ** b =", a ** b        ! exponentiation → 10^3 = 1000

  ! --- Relational Operators ---
  print *, "=== Relational Operators ==="
  print *, "a == b ?", a == b        ! equality
  print *, "a /= b ?", a /= b        ! not equal
  print *, "a > b ?", a > b
  print *, "a < b ?", a < b

  ! --- Logical Operators ---
  flag = (a > b) .AND. (x > y)
  print *, "=== Logical Operators ==="
  print *, "flag (a>b AND x>y) =", flag
  print *, "NOT flag =", .NOT. flag
  print *, "(a>b OR x<y) =", (a > b) .OR. (x < y)

  ! --- Functions Example ---
  print *, "=== Function Demo ==="
  z = square_root(x)   ! call our custom function below
  print *, "Square root of", x, "=", z

contains
  ! Custom function: returns square root
  real function square_root(num)
    real, intent(in) :: num
    square_root = sqrt(num)   ! using intrinsic sqrt()
  end function square_root

end program basics
