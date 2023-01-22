package com.webmvc.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.webmvc.model.Person;

@Controller
public class UserController {
	
	
	
	@RequestMapping(value="/displayPersonPage",method=RequestMethod.GET)
	public String displayUserPage(Model m){
		Person person=new Person();
		m.addAttribute("person",person);
		return "/PersonForm";
		
	}
	
	@RequestMapping(value="/personDetails",method=RequestMethod.POST)
	public String displayUserDetails(@ModelAttribute Person person,Model m){
		m.addAttribute("person",person);
		return "/personDetails";
	}
	
	
}
