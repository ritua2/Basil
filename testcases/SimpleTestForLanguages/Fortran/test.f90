! Fortran test case
program main
  integer :: a, b, result

  a = 2
  b = 3
  result = add(a, b)

  write(*, *) result ! Expected output: 5

contains

  function add(x, y) result(z)
    integer, intent(in) :: x, y
    integer :: z
    z = x + y
  end function add

end program main
