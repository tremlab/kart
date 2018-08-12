import React from 'react';
import $ from 'jquery';
import Kart from './Kart.jsx';
import Suggestions from './Suggestions.jsx';

class UserInput extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			userInput: '',
			kart: [],
			suggestions: []
		};
		this.handleInputAdd = this.handleInputAdd.bind(this);
		this.handleInputChange = this.handleInputChange.bind(this);
	}
	handleInputAdd(event) {
		event.preventDefault();
		const uInput = this.state.userInput
		console.log('adding...', uInput)

		if (uInput) {
			$.post(window.location.href + 'kartItem', {"userInput": uInput}, (data) => {
					this.setState({ kart: data })
			  });

			this.setState({
				userInput: ''
			});
		}
	}
	handleInputChange(event) {
		const value = event.target.value;
		this.setState({
			userInput: value
		});
		$.get(window.location.href + 'suggestions?userInput=' + value, (data) => {
				this.setState({ suggestions: data })
			});
	}

	render() {
		return (
			<div>
				<Suggestions suggestions={this.state.suggestions}/>
				<form className="Form">
					<input placeholder="start typing...." list="suggestions" type="text" value={this.state.userInput} onChange={this.handleInputChange} />
					<button onClick={this.handleInputAdd}>Add</button>
				</form>
				<Kart kart={this.state.kart}/>
			</div>
		);
	}
}


export default UserInput;