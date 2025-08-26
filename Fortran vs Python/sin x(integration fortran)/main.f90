program integration_methods
  implicit none
  integer, parameter :: dp = kind(1.0d0)
  integer :: i, n, start_time, end_time, count_rate
  real(dp) :: a, b, h, trapezoid_result, simpson_result, taylor_result
  real(dp), dimension(10) :: x_values, trapezoid_vals, simpson_vals, taylor_vals, exact_vals, times
  character(len=30), dimension(10) :: status

  ! Integration limits
  a = 0.0_dp
  b = acos(-1.0_dp)   ! pi
  n = 1000            ! intervals for numerical methods

  ! Generate test x values (for demonstration)
  do i = 1, 10
     x_values(i) = i * (b / 10.0_dp)
  end do

  ! Loop through test cases
  do i = 1, 10
     call system_clock(start_time, count_rate)

     trapezoid_result = trapezoid_rule(a, x_values(i), n)
     call system_clock(end_time)
     times(i) = real(end_time - start_time, dp) / real(count_rate, dp)
     trapezoid_vals(i) = trapezoid_result
     exact_vals(i) = -cos(x_values(i)) + cos(0.0_dp)   ! exact integral

     ! Simpson’s Rule
     call system_clock(start_time, count_rate)
     simpson_result = simpson_rule(a, x_values(i), n)
     call system_clock(end_time)
     times(i) = times(i) + real(end_time - start_time, dp) / real(count_rate, dp)
     simpson_vals(i) = simpson_result

     ! Taylor Series Approximation of sin(x)
     call system_clock(start_time, count_rate)
     taylor_result = taylor_integration(a, x_values(i), n)
     call system_clock(end_time)
     times(i) = times(i) + real(end_time - start_time, dp) / real(count_rate, dp)
     taylor_vals(i) = taylor_result

     ! Mark if floating-point limits exceeded
     if (abs(taylor_result) > huge(1.0_dp)) then
        status(i) = "exceeded limits"
     else
        status(i) = "ok"
     end if
  end do

  ! Print results dictionary-like format
  print *, "Results in format:"
  print *, '"input" : { "time taken", "Trapezoid", "Simpson", "Taylor", "Expected", "status"}'

  do i = 1, 10
     print *, "x=", x_values(i), ":{", times(i), ",", trapezoid_vals(i), ",", &
              simpson_vals(i), ",", taylor_vals(i), ",", exact_vals(i), ",", trim(status(i)), "}"
  end do

contains

  function f(x) result(val)
    real(dp), intent(in) :: x
    real(dp) :: val
    val = sin(x)
  end function f

  ! Trapezoidal rule
  function trapezoid_rule(a, b, n) result(integral)
    real(dp), intent(in) :: a, b
    integer, intent(in) :: n
    real(dp) :: integral, h, x
    integer :: i
    integral = 0.0_dp
    h = (b - a) / n
    integral = 0.5_dp * (f(a) + f(b))
    do i = 1, n - 1
       x = a + i * h
       integral = integral + f(x)
    end do
    integral = integral * h
  end function trapezoid_rule

  ! Simpson’s rule
    function simpson_rule(a, b, n) result(integral)
    real(dp), intent(in) :: a, b
    integer, intent(in) :: n
    real(dp) :: integral, h, x
    integer :: i, n_local
    n_local = n
    if (mod(n_local,2) /= 0) n_local = n_local + 1   ! Simpson requires even n
    h = (b - a) / n_local
    integral = f(a) + f(b)
    do i = 1, n_local - 1
       x = a + i * h
       if (mod(i,2) == 0) then
          integral = integral + 2.0_dp * f(x)
       else
          integral = integral + 4.0_dp * f(x)
       end if
    end do
    integral = integral * h / 3.0_dp
  end function simpson_rule

  ! Taylor Series Approximation of sin(x): sin(x) ≈ x - x^3/3! + x^5/5!
  ! Integrate term by term manually: ∫ sin(x) dx ≈ x^2/2 - x^4/(4*3!) + x^6/(6*5!)
  function taylor_integration(a, b, n) result(integral)
    real(dp), intent(in) :: a, b
    integer, intent(in) :: n
    real(dp) :: integral

    integral = (b**2 - a**2)/2.0_dp                        &
             - ((b**4 - a**4)/(24.0_dp))                   &
             + ((b**6 - a**6)/(720.0_dp))
  end function taylor_integration

end program integration_methods
