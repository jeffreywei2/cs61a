(define (rle s)
  (define (run elem st len)
    (cond ((null? st) (cons-stream (list elem len) nil))
        ((= elem (car st)) (run elem (cdr-stream st) (+ len 1)))
        (else (cons-stream (list elem len) (rle st))))
    )
    (if (null? s)
    nil
    (run (car  s) (cdr-stream s) 1))
)



(define (group-by-nondecreasing s)
  (define (tail lst last rest)
    (cond ((null? rest) (cons-stream lst nil))
    ((>= (car rest) last)
            (tail (append lst (list (car rest))) (car rest) (cdr-stream rest))
        )
        (else (cons-stream lst (tail (list (car rest)) (car rest) (cdr-stream rest))))
    )
  )
  (if (null? s) nil
    (tail (list (car s)) (car s) (cdr-stream s))
    )
)

(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

