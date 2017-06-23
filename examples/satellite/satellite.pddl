(define 
	(domain satellite)
	;(:requirements :equality :strips)
	;(:requirements :equality :strips :typing :invalid)
	(:requirements :equality :strips :typing)
	(:types tipo)
	;(:types tipo tipo)
	;(:constants c c2 - tipon)
	;(:constants c c - tipo)
	;(:constants - tipo)
	
	(:predicates
		 (on_board ?i ?s)
		 (supports ?i ?m)
		 (pointing ?s ?d)
		 (power_avail ?s)
		 (power_on ?i)
		 (calibrated ?i)
		 (have_image ?d ?m)
		 (calibration_target ?i ?d)
		 (satellite ?x)
		 (direction ?x)
		 (instrument ?x)
		 (mode ?x)
		 ;(mode ?x) ; redefinition
		 ;(testpredicate ?x - tipo)
		 ;(#testpredicate ?x - tipo)
		 ;(domain ?x) ; palavra reservada
	)
	;)


	(:functions
		;(road-length ?l1 ?l2 - tipo2)
		(road-length ?l1 ?l2 - tipo)
    	(total-cost2)
    	;(total-cost2)
		(total-cost ?ds - tipo) - tipo
		;(total-cost ?ds - tipo) - tipo
  	)

	(:action turn_to
		:parameters
			(?s ?d_new ?d_prev)
			;(?s ?d_new ?d_prev ?d_prev)
		:precondition
			(and 
				;(undefinedpred ?s)
				(satellite ?s)
				(direction ?d_new)
				(direction ?d_prev)
				(pointing ?s ?d_prev)
			)
		:effect
			(and
				(pointing ?s ?d_new)
				(not (pointing ?s ?d_prev))
			)
	)

	(:action switch_on
		:parameters 
			(?i ?s)
	 	:precondition
			(and 
				(instrument ?i)
				(satellite ?s)
				(on_board ?i ?s)
				(power_avail ?s)
			)
		:effect
			(and
				(power_on ?i)
				(not (calibrated ?i))
				(not (power_avail ?s))
			)
	)

	(:action switch_off
		:parameters 
			(?i ?s)
	 	:precondition
			(and 
				(instrument ?i) 
				(satellite ?s)  
				(on_board ?i ?s) 
				(power_on ?i)
			)
		:effect
			(and 
				(power_avail ?s)
				(not (power_on ?i))
			)
	)

	(:action calibrate
		:parameters 
			(?s ?i ?d)
	 	:precondition
			(and 
				(satellite ?s) 
				(instrument ?i) 
				(direction ?d)  
				(on_board ?i ?s) 
				(calibration_target ?i ?d) 
				(pointing ?s ?d) 
				(power_on ?i)
			)
	 	:effect
		 	(calibrated ?i)
	)

	(:action take_image
	 	:parameters 
	 		(?s ?d ?i ?m)
	 	:precondition
			(and 
				(satellite ?s) 
				(direction ?d) 
				(instrument ?i) 
				(mode ?m)  
				(calibrated ?i) 
				(on_board ?i ?s) 
				(supports ?i ?m) 
				(power_on ?i) 
				(pointing ?s ?d) 
				(power_on ?i)
			)
	 	:effect
			(have_image ?d ?m)
	)

	;(:action take_image ; action redefinition
	; 	:parameters 
	; 		(?s ?d ?i ?m)
	; 	:precondition
	;		(and 
	;			(satellite ?s) 
	;			(direction ?d) 
	;			(instrument ?i) 
	;			(mode ?m)  
	;			(calibrated ?i) 
	;			(on_board ?i ?s) 
	;			(supports ?i ?m) 
	;			(power_on ?i) 
	;			(pointing ?s ?d) 
	;			(power_on ?i)
	;		)
	; 	:effect
	;		(have_image ?d ?m)
	;)
)

