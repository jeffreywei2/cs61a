(define email "jeffreywei@berkeley.edu")

;; This question is in two parts, implementing `artisan-filter` and
;; `remove-comments`. See the specifications above each definition
;; for details.

;; You need to do part (a) to run the tests for part (b).

;; NOTE: In all scheme/sql questions you can put a multi-line answer
;;    in a blank


;; Part (a)
;; A artisan-filter is similar to a normal `filter` operation, except that
;; it involves deeply filtering the given list by removing all elements
;; that *do* match the predicate.
;;
;; NOTE 1: If the entire input matches the predicate, you should not delete it
;; NOTE 2: You can assume that `pred` can be called on an element of any type
;;
;; To run tests just for this part, run
;;      python3 ok -q a
;;
;; scm> (artisan-filter '(1 (2) (2 3)) (lambda (x) (and (number? x) (even? x))))
;; (1 () (3))
;; scm> (artisan-filter '(1 (2) (2 3) 4 5 6) list?)
;; (1 4 5 6)
;; scm> (artisan-filter '(1 2 3 4) list?)
;; (1 2 3 4)
;; scm> (artisan-filter '(i accidentally broke my computer) (lambda (x) (equal? x 'broke)))
;; (i accidentally my computer)
;; scm> (artisan-filter '(a (a) ((a)) (((a)))) (lambda (x) (equal? x 'a)))
;; (() (()) ((())))

(define (artisan-filter lst pred)
    (cond
        ((or (not (list? lst)) (null? lst))
            lst)
        ((pred (car lst))
            (artisan-filter (cdr lst) pred))
        (else
            (cons
                (artisan-filter (car lst) pred)
                (artisan-filter (cdr lst) pred)))))

;; Part (b)
;; Now implement the macro `remove-comments`, that takes in a piece of code
;; and evaluates it, ignoring the 'comments' within it.
;;
;; Comments are tagged lists that begin with the tag `comment-starting-symbol`
;;
;; scm> (remove-comments ((comment-starting-symbol hi) + 2 3))
;; 5
;; scm> (remove-comments '(this is (comment-starting-symbol even-when-quoted) a list))
;; (this is a list)
;; scm> (remove-comments '((this is not a comment comment-starting-symbol)))
;; ((this is not a comment comment-starting-symbol))

(define-macro (remove-comments code)
    (define (helper x)
        (and (list? x) (eq? (car x) 'comment-starting-symbol)))
    (artisan-filter code helper))

; ORIGINAL SKELETON FOLLOWS

; ;; This question is in two parts, implementing `artisan-filter` and
; ;; `remove-comments`. See the specifications above each definition
; ;; for details.

; ;; You need to do part (a) to run the tests for part (b).

; ;; NOTE: In all scheme/sql questions you can put a multi-line answer
; ;;    in a blank


; ;; Part (a)
; ;; A artisan-filter is similar to a normal `filter` operation, except that
; ;; it involves deeply filtering the given list by removing all elements
; ;; that *do* match the predicate.
; ;;
; ;; NOTE 1: If the entire input matches the predicate, you should not delete it
; ;; NOTE 2: You can assume that `pred` can be called on an element of any type
; ;;
; ;; To run tests just for this part, run
; ;;      python3 ok -q a
; ;;
; ;; scm> (artisan-filter '(1 (2) (2 3)) (lambda (x) (and (number? x) (even? x))))
; ;; (1 () (3))
; ;; scm> (artisan-filter '(1 (2) (2 3) 4 5 6) list?)
; ;; (1 4 5 6)
; ;; scm> (artisan-filter '(1 2 3 4) list?)
; ;; (1 2 3 4)
; ;; scm> (artisan-filter '(i accidentally broke my computer) (lambda (x) (equal? x 'broke)))
; ;; (i accidentally my computer)
; ;; scm> (artisan-filter '(a (a) ((a)) (((a)))) (lambda (x) (equal? x 'a)))
; ;; (() (()) ((())))

; (define (artisan-filter lst pred)
;     (cond
;         ((or (not (list? lst)) (null? lst))
;             ______)
;         ((pred ______)
;             (artisan-filter ______ ______))
;         (else
;             (cons
;                 ______
;                 ______))))

; ;; Part (b)
; ;; Now implement the macro `remove-comments`, that takes in a piece of code
; ;; and evaluates it, ignoring the 'comments' within it.
; ;;
; ;; Comments are tagged lists that begin with the tag `comment-starting-symbol`
; ;;
; ;; scm> (remove-comments ((comment-starting-symbol hi) + 2 3))
; ;; 5
; ;; scm> (remove-comments '(this is (comment-starting-symbol even-when-quoted) a list))
; ;; (this is a list)
; ;; scm> (remove-comments '((this is not a comment comment-starting-symbol)))
; ;; ((this is not a comment comment-starting-symbol))

; (define-macro (remove-comments code)
;     (define (helper x)
;         ______)
;     (artisan-filter ______ ______))
