program main
  implicit none
  integer, parameter :: dp = kind(1.0d0)
  real(dp) :: xvals(10) = (/ 0.1d0, 0.5d0, 1.0d0, 2.0d0, 3.14d0, 6.28d0, 10.0d0, 20.0d0, 50.0d0, 100.0d0 /)
  integer :: i
  real(dp) :: t_start, t_end, got, expected
  character(len=20) :: msg

  ! Loop over test values
  do i = 1, size(xvals)
     call cpu_time(t_start)

     got = cos_taylor_first(xvals(i))
     if (got /= -9999.0d0) then
        expected = cos(xvals(i))
        msg = ""
     else
        expected = -9999.0d0
        msg = "exceeded limits"
     end if

     call cpu_time(t_end)

     ! Structured print in dictionary style
     if (msg == "") then
        print '(A,F6.2,A,ES20.12,A,ES20.12,A,ES12.5)', &
              'x=', xvals(i), ': {"time_taken":', t_end - t_start, &
              ', "answer_got":', got, ', "answer_expected":', expected, '}'
     else
        print '(A,F6.2,A,F12.8,A,A)', 'x=', xvals(i), ': {"time_taken":', t_end - t_start, &
              ', "answer_got": exceeded limits, "answer_expected":', msg, '}'
     end if
  end do

contains

  recursive function factorial(n) result(res)
    integer, intent(in) :: n
    integer :: res
    if (n == 0) then
       res = 1
    else
       res = n * factorial(n-1)
    end if
  end function factorial

  function cos_taylor_first(x) result(res)
    real(dp), intent(in) :: x
    real(dp) :: res
    integer :: fact

    ! Try computing factorial(2) safely
    fact = factorial(2)
    if (fact > 0) then
       res = 1.0d0 - (x**2) / real(fact, dp)
    else
       res = -9999.0d0   ! flag for exceeded limits
    end if
  end function cos_taylor_first

end program main
